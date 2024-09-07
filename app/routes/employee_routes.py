from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.employee_schema import EmployeeCreate, Employee
from app.services import employee_services
from app.config.config import get_db
from app.models.task_model import Task

router = APIRouter()

@router.get("/employees/", response_model=list[Employee])
def get_employees(db: Session = Depends(get_db)):
    return employee_services.get_all_employees(db)


@router.post("/employees/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return employee_services.create_employee(db, employee.model_dump())


@router.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_services.delete_employee(db, employee_id)