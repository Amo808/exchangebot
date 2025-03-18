from fastapi import APIRouter, Query
from services import get_currency_rate, get_weather, get_news

router = APIRouter()

@router.get("/currency-rate")
async def currency_rate(
    from_currency: str = Query("USD", description="Исходная валюта"),
    to_currency: str = Query("EUR", description="Целевая валюта"),
    amount: float = Query(1.0, description="Количество валюты")
):
    return await get_currency_rate(from_currency, to_currency, amount)

@router.get("/weather")
async def weather(city: str = Query("London", description="Город для прогноза погоды")):
    return await get_weather(city)

@router.get("/news")
async def news():
    return await get_news()
