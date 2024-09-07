from sqlalchemy.orm import Session
from app.repositories import employee_repository, task_repository
from fastapi import HTTPException

def delete_employee(db: Session, employee_id: int):
    tasks = task_repository.get_tasks_by_employee(db, employee_id)
    if tasks:
        raise HTTPException(status_code=400, detail="Cannot delete an employee with assigned tasks")
    return employee_repository.delete_employee(db, employee_id)