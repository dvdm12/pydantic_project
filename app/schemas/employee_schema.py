from pydantic import BaseModel, EmailStr
from typing import List

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    tasks: List['Task'] = []

    class Config:
        orm_mode = True