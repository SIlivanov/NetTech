from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Практическая работа №5: CRUD и обработка ошибок",
    description="Разработчик: Иванов К.А."
)

# Подключаем только маршрутизатор задач
app.include_router(todo_router)


@app.get("/")
async def root() -> dict:
    return {"message": "API списка задач успешно запущено. Перейдите на /docs для тестирования."}
