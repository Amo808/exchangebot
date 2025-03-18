from app.services import get_currency_rate, get_weather, get_news
import pytest
import asyncio

@pytest.mark.asyncio
async def test_currency():
    result = await get_currency_rate("USD", "EUR", 1)
    assert "rates" in result

@pytest.mark.asyncio
async def test_weather():
    result = await get_weather("London")
    assert "location" in result

@pytest.mark.asyncio
async def test_news():
    result = await get_news()
    assert "news" in result