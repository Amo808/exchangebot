from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_currency_rate():
    response = client.get("/currency-rate?from_currency=USD&to_currency=EUR&amount=10")
    assert response.status_code == 200
    assert "error" not in response.json()

def test_weather():
    response = client.get("/weather?city=London")
    assert response.status_code == 200
    assert "error" not in response.json()

def test_news():
    response = client.get("/news")
    assert response.status_code == 200
    assert "error" not in response.json()