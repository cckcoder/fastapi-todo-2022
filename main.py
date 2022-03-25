from fastapi import FastAPI
from models.database import engine, Base
from routers.todo import todo_router

app = FastAPI()


app.include_router(todo_router.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}


Base.metadata.create_all(engine)
