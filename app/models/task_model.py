from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from app.config.config import Base



class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(100), index=True)
    status = Column(String(20), index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))


    employee = relationship("Employee", back_populates="tasks")


class TaskBase(BaseModel):
    id: int
    task_name: str
    status: str

    class Config:
        from_attributes = True