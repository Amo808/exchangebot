import httpx

# API-ключи
RAPIDAPI_KEY = "4bc55e00fbmshdf3198af3475aaap136df8jsn26a1c06c2582"

# API URL-адреса
METEOSTAT_API = "https://meteostat.p.rapidapi.com/point/monthly"
YFINANCE_QUOTES_API = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
YFINANCE_NEWS_API = "https://yahoo-finance166.p.rapidapi.com/api/news/list-by-symbol"

async def get_weather_history(lat: float, lon: float, alt: int, start: str, end: str):
    """
    Получение исторических погодных данных (месячные).
    """
    params = {"lat": lat, "lon": lon, "alt": alt, "start": start, "end": end}
    headers = {"x-rapidapi-host": "meteostat.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(METEOSTAT_API, headers=headers, params=params)
        return response.json()

async def get_stock_quotes(tickers: list):
    """
    Получение котировок акций по указанным тикерам.
    """
    tickers_str = ",".join(tickers)
    params = {"ticker": tickers_str}
    headers = {"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(YFINANCE_QUOTES_API, headers=headers, params=params)
        return response.json()

async def get_stock_news(tickers: list, region: str, snippet_count: int):
    """
    Получение новостей по тикерам.
    """
    tickers_str = ",".join(tickers)
    params = {"s": tickers_str, "region": region, "snippetCount": snippet_count}
    headers = {"x-rapidapi-host": "yahoo-finance166.p.rapidapi.com", "x-rapidapi-key": RAPIDAPI_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(YFINANCE_NEWS_API, headers=headers, params=params)
        return response.json()