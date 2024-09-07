from sqlalchemy.orm import Session
from app.repositories import task_repository
from fastapi import HTTPException


def create_task(db: Session, task_data):
    task_count = task_repository.get_task_count_by_employee(db, task_data["employee_id"])
    if task_count >= 10:
        raise HTTPException(status_code=400, detail="Employee has already reached the task limit.")

    if task_data["status"] not in ["pending task", "task completed"]:
        raise HTTPException(status_code=400, detail="Invalid task status.")

    return task_repository.create_task(db, task_data)