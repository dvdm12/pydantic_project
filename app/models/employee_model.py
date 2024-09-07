from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="employee")