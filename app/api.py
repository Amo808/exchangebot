from fastapi import APIRouter, Query
from app.services import get_weather_history, get_stock_quotes, get_stock_news

router = APIRouter()

@router.get("/weather-history")
async def weather_history(
    lat: float = 52.5244,
    lon: float = 13.4105,
    alt: int = 43,
    start: str = "2020-01-01",
    end: str = "2020-12-31"
):
    return await get_weather_history(lat, lon, alt, start, end)

@router.get("/stock-quotes")
async def stock_quotes(tickers: str = Query("AAPL,MSFT,GAZP.ME")):
    tickers_list = tickers.split(",")
    return await get_stock_quotes(tickers_list)

@router.get("/stock-news")
async def stock_news(
    tickers: str = Query("AAPL,GOOGL,TSLA"),
    region: str = "US",
    snippet_count: int = 10
):
    tickers_list = tickers.split(",")
    return await get_stock_news(tickers_list, region, snippet_count)