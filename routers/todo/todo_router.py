from imp import get_frozen_object
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from models.scheme import TodoBase, TodoDisplay
from models.database import get_db

from . import todo_controller

router = APIRouter(prefix="/todo", tags=["todo"])


@router.get("/", response_model=List[TodoDisplay])
def all_todo(db: Session = Depends(get_db)):
    return todo_controller.get_all_todo(db)

@router.get("/{id}", response_model=TodoDisplay)
def todo(id: int, db: Session = Depends(get_db)):
    return todo_controller.todo_by_id(db, id)


@router.post("/", response_model=TodoBase)
def create_todo(request: TodoBase, db: Session = Depends(get_db)):
    return todo_controller.create_todo(db, request)


@router.put("/{id}", response_model=TodoBase)
def update_todo(id: int, request: TodoBase, db: Session = Depends(get_db)):
    return todo_controller.update_todo(db, id, request)


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    return todo_controller.delete_todo(db, id)
