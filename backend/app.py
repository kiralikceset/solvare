"""
app.py - Flask backend for AI Kaos D\u00fczenleyici

Nas\u0131l \u00e7al\u0131\u015ft\u0131r\u0131l\u0131r?
1. Python ve pip y\u00fcklenmi\u015f olmal\u0131d\u0131r.
2. Gerekli k\u00fct\u00fcphaneleri kurun: `pip install -r backend/requirements.txt`
3. Ortam de\u011fi\u015fkenlerini ayarlay\u0131n (OpenAI, Google, vb.).
4. Uygulamay\u0131 ba\u015flat\u0131n: `python backend/app.py`

Bu dosya Flask uygulamas\u0131n\u0131, veritaban\u0131 ba\u011flant\u0131s\u0131n\u0131 ve
AI tabanl\u0131 plan olu\u015fturma endpoint'ini tan\u0131mlar.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from db import db, init_db
from models import User, Plan
from api_clients import (
    generate_plan_with_openai,
    generate_image_with_dalle,
    get_weather,
    get_spotify_playlist,
    get_calendar_events,
)

# .env dosyas\u0131ndan anahtarlar\u0131 y\u00fckle
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Uygulama ba\u015flarken veritaban\u0131n\u0131 olu\u015ftur
with app.app_context():
    init_db()


@app.route("/api/plan", methods=["POST"])
def create_plan():
    """\n    Kullan\u0131c\u0131n\u0131n giri\u015f verilerini al\u0131r, OpenAI API'si ile mikro plan \u00fcretir
    ve DALL-E 3 API'si ile bir g\u00f6rsel oluturur. Plan veritaban\u0131na kaydedilir.
    """

    data = request.get_json() or {}
    mood = data.get("mood", "N\u00f6tr")
    time_available = data.get("time_available", "1 saat")
    activities = data.get("activities", [])
    location = data.get("location", "Istanbul")

    # Harici API'lardan ek veriler (hava durumu, takvim, Spotify)
    weather = get_weather(location)
    calendar = get_calendar_events()
    playlist = get_spotify_playlist(mood)

    # Plan \u00fcret
    plan_text = generate_plan_with_openai(
        mood=mood,
        time_available=time_available,
        activities=activities,
        location=location,
        weather=weather,
        calendar=calendar,
    )
    image_url = generate_image_with_dalle(plan_text)

    plan = Plan(
        mood=mood,
        time_available=time_available,
        activities=",".join(activities),
        plan_text=plan_text,
        image_url=image_url,
    )
    db.session.add(plan)
    db.session.commit()

    return jsonify(
        {
            "plan": plan_text,
            "image_url": image_url,
            "playlist": playlist,
            "weather": weather,
        }
    )


@app.route("/api/points", methods=["POST"])
def add_points():
    """Kullan\u0131c\u0131n\u0131n oyunda kazand\u0131\u011f\u0131 puanlar\u0131 kaydeder."""

    data = request.get_json() or {}
    user_id = data.get("user_id")
    points = data.get("points", 0)

    user = User.query.get(user_id)
    if not user:
        user = User(id=user_id, points=0)
        db.session.add(user)

    user.points += points
    db.session.commit()

    return jsonify({"points": user.points})


if __name__ == "__main__":
    app.run(debug=True)

