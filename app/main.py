from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="ExchangeBot",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router)  # Верни маршруты!

@app.get("/")
def read_root():
    return {"message": "ExchangeBot is running!"}
