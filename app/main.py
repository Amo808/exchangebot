from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="MCP Server",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)