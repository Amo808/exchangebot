from fastapi import APIRouter, Query
from app.services import get_currency_rate, get_weather, get_news

router = APIRouter()

@router.get("/currency-rate")
async def currency_rate(
    from_currency: str = "USD",
    to_currency: str = "EUR",
    amount: float = 1.0
):
    return await get_currency_rate(from_currency, to_currency, amount)

@router.get("/weather")
async def weather(city: str = "London"):
    return await get_weather(city)

@router.get("/news")
async def news():
    return await get_news()
