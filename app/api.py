from fastapi import APIRouter
from app.services import get_exchange_rate, get_weather, get_news

router = APIRouter()

@router.get("/exchange-rate")
async def exchange_rate():
    return await get_exchange_rate()

@router.get("/weather/{city}")
async def weather(city: str):
    return await get_weather(city)

@router.get("/news")
async def news():
    return await get_news()