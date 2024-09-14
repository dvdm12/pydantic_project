from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.employee_schema import EmployeeDto
from app.services import employee_services
from app.config.config import get_db

router = APIRouter()

@router.get("/", response_model=list[EmployeeDto])
def get_employees(db: Session = Depends(get_db)):
    return employee_services.get_all_employees(db)


@router.post("/", response_model=EmployeeDto)
def create_employee(employee: EmployeeDto, db: Session = Depends(get_db)):
    return employee_services.create_employee(db, employee.model_dump())


@router.delete("/{employee_id}", response_model=EmployeeDto)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_services.delete_employee(db, employee_id)