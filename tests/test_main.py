from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_exchange_rate():
    response = client.get("/exchange-rate")
    assert response.status_code == 200

def test_weather():
    response = client.get("/weather/Moscow")
    assert response.status_code == 200

def test_news():
    response = client.get("/news")
    assert response.status_code == 200
