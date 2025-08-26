"""
models.py - Uygulaman\u0131n veritaban\u0131 modelleri

Bu dosyada kullan\u0131c\u0131 (User) ve plan (Plan) tablolar\u0131 tan\u0131mlan\u0131r.
"""

from datetime import datetime
from db import db


class User(db.Model):
    """Kullan\u0131c\u0131 bilgilerini ve puanlar\u0131n\u0131 saklar."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    points = db.Column(db.Integer, default=0)


class Plan(db.Model):
    """AI taraf\u0131ndan olu\u015fturulan mikro planlar."""

    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(80))
    time_available = db.Column(db.String(80))
    activities = db.Column(db.String(200))
    plan_text = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    user = db.relationship("User", backref=db.backref("plans", lazy=True))

