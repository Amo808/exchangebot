import httpx
import os

EXCHANGE_API = "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD"
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
NEWS_API = "https://newsapi.org/v2/everything?q=world&from=2024-09-15&sortBy=publishedAt&apiKey=YOUR-API-KEY"

async def get_exchange_rate():
    async with httpx.AsyncClient() as client:
        response = await client.get(EXCHANGE_API)
        data = response.json()
        return {"USD_to_RUB": data["conversion_rates"]["RUB"]}

async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{WEATHER_API}?q={city}&appid=YOUR-API-KEY&units=metric")
        data = response.json()
        return {"city": city, "temperature": data["main"]["temp"], "condition": data["weather"][0]["description"]}

async def get_news():
    async with httpx.AsyncClient() as client:
        response = await client.get(NEWS_API)
        data = response.json()
        return {"articles": data["articles"][:5]}
