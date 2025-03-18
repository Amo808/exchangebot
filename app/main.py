from fastapi import FastAPI
from app.api import router

app = FastAPI(title="MCP Server")

app.include_router(router)