from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    # Конфигурация для Swagger/ReDoc с примером заполнения
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "item": "Пример задачи студента (Константин Иванов)"
            }
        }
    }
