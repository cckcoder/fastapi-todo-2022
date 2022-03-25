from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from models.todo_model import DbTodo

from models.scheme import TodoBase


def create_todo(db: Session, request: TodoBase):
    new_todo = DbTodo(text=request.text, completed=request.completed)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todo(db: Session):
    todos = db.query(DbTodo).all()
    return todos
