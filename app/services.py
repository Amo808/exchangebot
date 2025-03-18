import httpx
import datetime

# API-ключ
RAPIDAPI_KEY = "4bc55e00fbmshdf3198af3475aaap136df8jsn26a1c06c2582"

# API URL-адреса
WEATHER_API = "https://weather-api-by-any-city.p.rapidapi.com/weather"
CURRENCY_API = "https://currency-converter5.p.rapidapi.com/currency/convert"
NEWS_API = "https://reuters-business-and-financial-news.p.rapidapi.com/market-rics/list-rics-by-asset-and-category"

async def get_currency_rate(from_currency: str, to_currency: str, amount: float):
    """
    Получение текущего курса валют.
    """
    params = {"format": "json", "from": from_currency, "to": to_currency, "amount": amount, "language": "en"}
    headers = {"x-rapidapi-host": "currency-converter5.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(CURRENCY_API, headers=headers, params=params)
        return response.json()

async def get_weather(city: str):
    """
    Получение прогноза погоды для указанного города.
    """
    headers = {"x-rapidapi-host": "weather-api-by-any-city.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{WEATHER_API}/{city}", headers=headers)
        return response.json()

async def get_news():
    """
    Получение новостей за последнюю неделю.
    """
    headers = {"x-rapidapi-host": "reuters-business-and-financial-news.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    last_week = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    params = {"date": last_week}

    async with httpx.AsyncClient() as client:
        response = await client.get(NEWS_API, headers=headers, params=params)
        return response.json()
