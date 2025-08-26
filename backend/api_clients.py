"""
api_clients.py - Harici servislerle ileti\u015fim fonksiyonlar\u0131

Bu dosya OpenAI, OpenWeatherMap, Spotify ve Google Calendar API'leri ile
nas\u0131l ba\u011flant\u0131 kurulaca\u011f\u0131n\u0131 g\u00f6steren \u00f6rnek fonksiyonlar i\u00e7erir.
Ger\u00e7ek API anahtarlar\u0131n\u0131 .env dosyan\u0131za ekleyin.
"""

import os
import requests
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY", "")
SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN", "")


def generate_plan_with_openai(mood, time_available, activities, location, weather, calendar):
    """OpenAI GPT-4o ile mikro plan \u00fcretir."""
    if not openai.api_key:
        # API anahtar\u0131 yoksa örnek bir plan d\u00f6n
        return "18:00'da evde film izle, 19:00'da yak\u0131n restoranda yemek ye"

    prompt = (
        f"Mood: {mood}\nTime: {time_available}\nActivities: {activities}\n"
        f"Location: {location}\nWeather: {weather}\nCalendar: {calendar}\n"
        "Bu bilgilere g\u00f6re saat saat plan haz\u0131rla."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"].strip()


def generate_image_with_dalle(plan_text):
    """DALL-E 3 ile plan\u0131n komik bir g\u00f6rselini üretir."""
    if not openai.api_key:
        return "https://placekitten.com/300/300"  # Yer tutucu görsel

    image = openai.Image.create(prompt=f"comic style: {plan_text}", n=1, size="512x512")
    return image["data"][0]["url"]


def get_weather(city):
    """OpenWeatherMap API'sinden hava durumu al."""
    if not OPENWEATHER_KEY:
        return "Güneşli"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric&lang=tr"
    resp = requests.get(url, timeout=10)
    data = resp.json()
    return data.get("weather", [{"description": "bilinmiyor"}])[0]["description"]


def get_spotify_playlist(mood):
    """Spotify API kullanarak ruh haline göre öneri listesi al."""
    if not SPOTIFY_TOKEN:
        return "https://open.spotify.com/playlist/example"
    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}
    params = {"q": mood, "type": "playlist", "limit": 1}
    resp = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params, timeout=10)
    data = resp.json()
    items = data.get("playlists", {}).get("items", [])
    return items[0]["external_urls"]["spotify"] if items else None


def get_calendar_events():
    """Google Calendar API'sinden kullanıcı etkinliklerini çeker.
    Bu \u00f6rnek yalnızca entegrasyon için yer tutucudur.
    """
    # Normalde OAuth2 ile kullanıcının takvimine erişip etkinlikleri listelersiniz.
    return ["18:00 Toplantı", "20:00 Arkadaşlarla buluşma"]

