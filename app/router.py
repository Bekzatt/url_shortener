from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, HttpUrl
from database import get_db
from services import generate_short_id
from storage import save_url, get_url
import os

router = APIRouter()
BASE_URL = os.getenv("BASE_URL")

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    short_url: str

@router.post(
    "/",
    response_model=URLResponse,
    status_code=201,
    summary="Сократить URL",
    description="Принимает исходный URL, сохраняет его в базе и возвращает сокращённую ссылку."
)
async def shorten_url(request: URLRequest, db: AsyncSession = Depends(get_db)):
    """
    Создаёт короткий URL.

    Получает URL из тела запроса, генерирует уникальный идентификатор,
    сохраняет в базе данных и возвращает короткий URL.
    """
    short_id = generate_short_id(request.url)
    await save_url(db, short_id, request.url)
    return URLResponse(short_url=f"{BASE_URL}/{short_id}")


@router.get(
    "/{short_id}",
    summary="Редирект по короткой ссылке",
    description="По идентификатору короткой ссылки возвращает оригинальный URL с редиректом (HTTP 307)."
)
async def redirect(short_id: str, db: AsyncSession = Depends(get_db)):
    """
    Редирект на оригинальный URL.

    Ищет оригинальный URL в базе данных по `short_id` и перенаправляет на него
    с использованием 307 Temporary Redirect.
    """
    original_url = await get_url(db, short_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url, status_code=307)