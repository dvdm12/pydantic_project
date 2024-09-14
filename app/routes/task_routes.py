from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskDto
from app.services import task_services
from app.config.config import get_db


router = APIRouter()

@router.get("/", response_model=list[TaskDto])
def get_tasks(db: Session = Depends(get_db)):
    return task_services.get_all_tasks(db)

@router.post("/", response_model=TaskDto)
def create_task(task: TaskDto, db: Session = Depends(get_db)):
    return task_services.create_task(db, task.model_dump())

@router.delete("/{task_id}", response_model=TaskDto)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_services.delete_task(db, task_id)