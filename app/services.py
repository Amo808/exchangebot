import httpx
from httpx import HTTPError
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# API URL-адреса
WEATHER_API = "https://weather-api-by-any-city.p.rapidapi.com/weather"
CURRENCY_API = "https://currency-converter5.p.rapidapi.com/currency/convert"
NEWS_API = "https://reuters-business-and-financial-news.p.rapidapi.com/market-rics/list-rics-by-asset-and-category"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY
}

async def get_currency_rate(from_currency: str, to_currency: str, amount: float):
    """
    Получение текущего курса валют.
    """
    params = {"format": "json", "from": from_currency, "to": to_currency, "amount": amount, "language": "en"}
    HEADERS["x-rapidapi-host"] = "currency-converter5.p.rapidapi.com"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(CURRENCY_API, headers=HEADERS, params=params)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

async def get_weather(city: str):
    """
    Получение прогноза погоды для указанного города.
    """
    params = {"city": city}
    HEADERS["x-rapidapi-host"] = "weather-api-by-any-city.p.rapidapi.com"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(WEATHER_API, headers=HEADERS, params=params)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}

async def get_news():
    """
    Получение новостей.
    """
    HEADERS["x-rapidapi-host"] = "reuters-business-and-financial-news.p.rapidapi.com"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(NEWS_API, headers=HEADERS)
            response.raise_for_status()
            return response.json()
    except HTTPError as e:
        return {"error": str(e)}