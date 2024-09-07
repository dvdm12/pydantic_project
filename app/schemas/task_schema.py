from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    task_name: str
    status: str
    employee_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
