from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    # Замените на ваши реальные Имя и Фамилию
    return {"message": "jooihph[j"}