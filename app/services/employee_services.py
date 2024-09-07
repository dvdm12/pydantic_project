from sqlalchemy.orm import Session
from app.repositories import employee_repository, task_repository
from fastapi import HTTPException

def delete_employee(db: Session, employee_id: int):
    tasks = task_repository.get_task_by_employee(db, employee_id)
    if tasks:
        raise HTTPException(status_code=400, detail="Cannot delete employee with assigned tasks.")
    return employee_repository.delete_employee(db, employee_id)


def create_employee(db: Session, employee_data):
    existing_employee = employee_repository.get_employees_by_id(db, employee_data["email"])
    if existing_employee:
        raise HTTPException(status_code=400, detail="Email already in use.")
    return employee_repository.create_employee(db, employee_data)


def get_all_employees(db: Session):
    employees = employee_repository.get_all_employees(db)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found.")
    return employees