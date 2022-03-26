from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

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


def todo_by_id(db: Session, id: int):
    todo = db.query(DbTodo).filter(DbTodo.id == id).first()
    return todo


def update_todo(db: Session, id: int, request: TodoBase):
    todo = db.query(DbTodo).filter(DbTodo.id == id).first()
    todo.text = request.text
    todo.completed = request.completed
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, id: int):
    todo = db.query(DbTodo).filter(DbTodo.id == id).first()
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )
    else:
        db.delete(todo)
        db.commit()
        return JSONResponse(
            content={"detail": f"Todo with id {id} deleted successfully"},
            status_code=status.HTTP_200_OK,
        )
