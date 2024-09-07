from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.config import Base
from app.schemas.task_schema import Task


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)

    tasks = relationship("Task", back_populates="employee")