from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, Task
from app.services import task_services
from app.config.config import get_db

router = APIRouter()

@router.get("/tasks/", response_model=list[Task])
def get_tasks(db: Session = Depends(get_db)):
    return task_services.get_all_tasks(db)

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_services.create_task(db, task.dict())

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_services.delete_task(db, task_id)