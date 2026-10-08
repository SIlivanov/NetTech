from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Todo API",
    description="Практическая работа №4 — Маршрутизация в FastAPI"
)

# Персонализированный корневой маршрут
@app.get("/")
async def welcome() -> dict:
    return {"message": "Добро пожаловать в приложение Todo! Автор: Константин Иванов"}

# Подключение маршрутов из todo_router
app.include_router(todo_router)
