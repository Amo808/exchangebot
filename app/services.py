import httpx
import os
from dotenv import load_dotenv
from httpx import HTTPError

# Загружаем переменные окружения
load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

if not RAPIDAPI_KEY:
    raise ValueError("API ключ не найден в .env файле!")

# API URL-адреса
WEATHER_API = "https://weather-api-by-any-city.p.rapidapi.com/weather"
CURRENCY_API = "https://currency-converter5.p.rapidapi.com/currency/convert"
NEWS_API = "https://reuters-business-and-financial-news.p.rapidapi.com/market-rics/list-rics-by-asset-and-category"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY
}

async def get_currency_rate(from_currency: str, to_currency: str, amount: float):
    params = {"format": "json", "from": from_currency, "to": to_currency, "amount": amount, "language": "en"}
    headers = {**HEADERS, "x-rapidapi-host": "currency-converter5.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(CURRENCY_API, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

async def get_weather(city: str):
    headers = {**HEADERS, "x-rapidapi-host": "weather-api-by-any-city.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{WEATHER_API}/{city}", headers=headers)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

async def get_news():
    headers = {**HEADERS, "x-rapidapi-host": "reuters-business-and-financial-news.p.rapidapi.com"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(NEWS_API, headers=headers)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}
