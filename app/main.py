"""
Главная точка входа в приложение FastAPI.

Настраивает запуск и подключает маршруты.
"""

from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from database import init_db
from router import router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Инициализация базы данных при старте приложения."""
    await init_db()
    yield

app = FastAPI(title="URL Shortener", lifespan=lifespan)

# Подключаем маршруты
app.include_router(router)
