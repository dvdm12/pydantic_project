from fastapi import FastAPI
from app.models import employee_model, task_model



# FastAPI instance
app = FastAPI(
    title="Employee and Task Management API",
    description="API for managing employees and tasks using FastAPI, MariaDb, SQLAlchemy, and Alembic.",
    version="1.0.0"
)