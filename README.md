# MCP Server

## Установка

```sh
pip install -r requirements.txt
Запуск локально
sh
Копировать
Редактировать
uvicorn app.main:app --reload
Доступные эндпоинты
/exchange-rate – Курс доллара
/weather/{city} – Погода в городе
/news – Новости
yaml
Копировать
Редактировать

---

### 9. **Запуск проекта локально**  
Запусти сервер командой:

```sh
uvicorn app.main:app --reload
Проверить работу можно по ссылкам:

http://127.0.0.1:8000/exchange-rate
http://127.0.0.1:8000/weather/Moscow
http://127.0.0.1:8000/news