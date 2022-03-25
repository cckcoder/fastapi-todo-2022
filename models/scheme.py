from datetime import datetime
from pydantic import BaseModel


class TodoBase(BaseModel):
    text: str
    completed: bool

    class Config:
        orm_mode = True


class TodoDisplay(BaseModel):
    text: str
    completed: bool
    date_created: datetime
    date_updated: datetime

    class Config:
        orm_mode = True
