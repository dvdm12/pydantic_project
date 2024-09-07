from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    status = Column(String, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="tasks")