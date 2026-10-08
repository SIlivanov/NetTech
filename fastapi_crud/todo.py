from fastapi import APIRouter, Path, HTTPException, status
from typing import List
from model import Todo, TodoItem, TodoItems

# Персонализация разработчика
DEV_NAME = "Разработчик Иванов К.А."

todo_router = APIRouter()
todo_list: List[Todo] = []


# 1. Добавление задачи (со статусом 201 Created)
@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": f"[{DEV_NAME}]: Задача успешно добавлена в список."
    }


# 2. Получение списка всех задач (с использованием response_model)
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }


# 3. Получение одной задачи по ID с обработкой 404
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="Идентификатор задачи для получения")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"[{DEV_NAME}]: Задача с ID={todo_id} не найдена в системе."
    )


# 4. Обновление задачи по ID с обработкой 404
@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="Идентификатор задачи для обновления")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": f"[{DEV_NAME}]: Задача с ID={todo_id} успешно обновлена."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"[{DEV_NAME}]: Ошибка обновления. Задача с ID={todo_id} не существует."
    )


# 5. Удаление одной задачи по ID с обработкой 404
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": f"[{DEV_NAME}]: Задача с ID={todo_id} успешно удалена."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"[{DEV_NAME}]: Невозможно удалить: задача с ID={todo_id} отсутствует."
    )


# 6. Удаление всех задач
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": f"[{DEV_NAME}]: Все задачи успешно очищены."
    }
