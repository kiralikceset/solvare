"""
Basit Flask endpoint testleri.
Calistirmak icin: `pytest`
"""

import pytest
from backend.app import app, db


@pytest.fixture
def client():
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    with app.app_context():
        db.create_all()
    return app.test_client()


def test_create_plan(client):
    response = client.post(
        "/api/plan",
        json={"mood": "Enerjik", "time_available": "2 saat", "activities": ["film"], "location": "Istanbul"},
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "plan" in data
    assert "image_url" in data

