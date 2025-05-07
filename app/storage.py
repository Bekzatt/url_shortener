"""
Функции для сохранения и получения URL из базы данных.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import ShortURL

async def save_url(db: AsyncSession, short_id: str, original_url: str):
    """
    Сохраняет пару (short_id, original_url) в базу данных.
    """
    try:
        db_url = ShortURL(short_id=short_id, original_url=str(original_url))
        db.add(db_url)
        await db.commit()
    except Exception as e:
        print("Error:",e)
        await db.rollback()

async def get_url(db: AsyncSession, short_id: str) -> str | None:
    """
    Возвращает оригинальный URL по short_id, если он существует.
    """
    result = await db.execute(select(ShortURL).where(ShortURL.short_id == short_id))
    short_url = result.scalars().first()
    return short_url.original_url if short_url else None
