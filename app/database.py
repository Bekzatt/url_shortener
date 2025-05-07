"""
Модуль работы с базой данных PostgreSQL с использованием SQLAlchemy.
"""

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Создание асинхронного движка PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# Асинхронная сессия для работы с БД
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для моделей
Base = declarative_base()

async def init_db():
    """Создаёт все таблицы при запуске приложения."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncSession:
    """Dependency-функция для получения сессии БД в маршрутах."""
    async with SessionLocal() as session:
        yield session
