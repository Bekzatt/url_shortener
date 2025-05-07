# 🔗 URL Shortener API

Проект на FastAPI для сокращения URL-адресов с хранением в PostgreSQL и асинхронной обработкой. Использует SQLAlchemy, Docker, .env и автогенерируемую Swagger-документацию.

---

![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)  
![FastAPI](https://img.shields.io/badge/fastapi-async--ready-green?logo=fastapi)  
![PostgreSQL](https://img.shields.io/badge/postgresql-db-blue?logo=postgresql)  
![Python](https://img.shields.io/badge/python-3.11+-blue?logo=python)

---

## 🚀 Возможности

- 📥 POST \`/\` — Сократить URL  
- 🔁 GET \`/{short_id}\` — Перенаправление на оригинальный URL  
- 📚 Swagger UI — доступен по адресу \`/docs\`  

---

## 🧱 Стек технологий

- **FastAPI** — веб-фреймворк  
- **PostgreSQL** — база данных  
- **SQLAlchemy (Async)** — ORM  
- **Uvicorn** — сервер ASGI  
- **Docker + Docker Compose**  
- **Pydantic, dotenv**  

---

## ⚙️ Установка и запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Bekzatt/url-shortener.git
cd url-shortener
```

### 2. Создайте .env файл
```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/url_shortener
BASE_URL=http://localhost:8080
```

### 3. Запустите приложение через Docker
```bash
docker-compose up --build
```

Приложение будет доступно по адресу:  
👉 http://localhost:8080  
Swagger документация:  
👉 http://localhost:8080/docs  

---

## 📤 Примеры использования

### 🔗 Сократить URL
**Запрос:**
```bash
POST/
```

**Тело запроса:**
```json
{
  "url": "https://example.com"
}
```

**Ответ:**
```json
{
  "short_url": "http://localhost:8080/1a2b3c4d"
}
```

### 🔁 Редирект по короткому URL
**Запрос:**
```bash
GET /1a2b3c4d
```

**Ответ:**  
307 Temporary Redirect → https://example.com  

---

## 🧾 Структура проекта
```
.
├── app/
│   ├── main.py          # Точка входа
│   ├── router.py        # Все маршруты
│   ├── database.py      # Подключение к БД
│   ├── models.py        # SQLAlchemy модели
│   ├── storage.py       # CRUD операции
│   ├── services.py      # Генерация short_id
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

## 🧪 Запуск без Docker (локально)
1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите сервер:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```