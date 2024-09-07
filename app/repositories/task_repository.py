from sqlalchemy.orm import Session
from app.models.task_model import Task

#Retrieves all task records from the database.
# Returns a list of Task objects
def get_all_tasks(db: Session):
    return db.query(Task).all()


#Creates a new task in the database using the provided task_data.
# Commits the new Task to the database and refreshes it to update any computed fields.
# Returns the newly created Task object.
def create_task(db: Session, task_data):
    new_task = Task(**task_data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

#Deletes a task identified by task_id from the database.
# If the task exists, it is removed and the change is committed.
# Returns the deleted Task object if found; otherwise, returns None
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

# Count employee tasks
def get_task_by_employee(db: Session, employee_id: int):
    return db.query(Task).filter(Task.employee_id == employee_id).all()

# Count employee tasks
def get_task_count_by_employee(db: Session, employee_id: int):
    return db.query(Task).filter(Task.employee_id == employee_id).count()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task