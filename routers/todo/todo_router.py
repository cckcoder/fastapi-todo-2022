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


@router.post("/", response_model=TodoBase)
def create_todo(request: TodoBase, db: Session = Depends(get_db)):
    return todo_controller.create_todo(db, request)
