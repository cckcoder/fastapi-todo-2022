from sqlalchemy import Column
from models.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from sqlalchemy.sql import func


class DbTodo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    completed = Column(Boolean, default=False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
