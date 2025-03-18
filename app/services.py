import httpx

# API Keys
RAPIDAPI_KEY = "4bc55e00fbmshdf3198af3475aaap136df8jsn26a1c06c2582"

# API Endpoints
METEOSTAT_API = "https://meteostat.p.rapidapi.com/point/monthly"
YFINANCE_QUOTES_API = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
YFINANCE_NEWS_API = "https://yahoo-finance166.p.rapidapi.com/api/news/list-by-symbol"

async def get_weather_history(lat: float, lon: float, alt: int, start: str, end: str):
    """Получает исторические данные о погоде (месячные)."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            METEOSTAT_API,
            headers={
                "x-rapidapi-host": "meteostat.p.rapidapi.com",
                "x-rapidapi-key": RAPIDAPI_KEY,
            },
            params={
                "lat": lat,
                "lon": lon,
                "alt": alt,
                "start": start,
                "end": end,
            }
        )
        return response.json()

async def get_stock_quotes(tickers: list):
    """Получает котировки акций по списку тикеров."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            YFINANCE_QUOTES_API,
            headers={
                "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
                "x-rapidapi-key": RAPIDAPI_KEY,
            },
            params={"ticker": ",".join(tickers)}
        )
        return response.json()

async def get_stock_news(tickers: list, region: str = "US", snippet_count: int = 10):
    """Получает новости по тикерам акций."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            YFINANCE_NEWS_API,
            headers={
                "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com",
                "x-rapidapi-key": RAPIDAPI_KEY,
            },
            params={
                "s": ",".join(tickers),
                "region": region,
                "snippetCount": snippet_count,
            }
        )
        return response.json()

# Пример вызова:
# weather_data = await get_weather_history(52.5244, 13.4105, 43, "2020-01-01", "2020-12-31")
# stock_quotes = await get_stock_quotes(["AAPL", "MSFT", "GAZP.ME"])
# stock_news = await get_stock_news(["AAPL", "GOOGL", "TSLA"])