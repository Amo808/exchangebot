📌 Файл requirements.txt
nginx
Копировать
Редактировать
fastapi
uvicorn
httpx
📌 Файл README.md (инструкция по запуску)
md
Копировать
Редактировать
# MCP Server

Этот сервер позволяет получать:
- Текущий курс валют
- Прогноз погоды в указанном городе
- Сводку новостей за последнюю неделю

## 🚀 Установка и запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
Запустите сервер:
bash
Копировать
Редактировать
python main.py
API-документация доступна по адресу:
Swagger: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
🛠 API Эндпоинты
Получение курса валют
bash
Копировать
Редактировать
GET /currency-rate?from_currency=USD&to_currency=EUR&amount=1
Получение погоды
bash
Копировать
Редактировать
GET /weather?city=London
Получение новостей
bash
Копировать
Редактировать
GET /news
yaml
Копировать
Редактировать

---

## 📌 **Как протестировать API**
1. Установите `pytest`:
   ```bash
   pip install pytest
Создайте test_services.py:
python
Копировать
Редактировать
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
Запустите тесты:
bash
Копировать
Редактировать
pytest test_services.py