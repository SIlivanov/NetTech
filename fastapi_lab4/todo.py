from fastapi import APIRouter, Path, HTTPException
from model import Todo

todo_router = APIRouter()

# Временная база данных (список в памяти)
todo_list = []

# 1. Добавление новой задачи (POST)
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Задача успешно добавлена (выполнил: Константин Иванов)"}

# 2. Получение всех задач (GET)
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

# 3. Получение одной задачи по ID (GET с Path-параметром)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="ID задачи, которую нужно получить", ge=1)
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": f"Задача с ID {todo_id} не найдена!"}

# 4. Обновление задачи (PUT) — упомянуто на стр. 12
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: Todo, todo_id: int = Path(..., ge=1)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Задача успешно обновлена"}
    return {"message": f"Задача с ID {todo_id} не найдена!"}

# 5. Удаление задачи (DELETE) — упомянуто на стр. 12
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., ge=1)) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Задача успешно удалена"}
    return {"message": f"Задача с ID {todo_id} не найдена!"}
