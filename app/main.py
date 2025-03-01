from fastapi import FastAPI
from app.models import employee_model, task_model
from app.routes import employee_routes, task_routes

# FastAPI instance
app = FastAPI(
    title="Employee and Task Management API",
    description="API for managing employees and tasks using FastAPI, MariaDb, SQLAlchemy, and Alembic.",
    version="1.0.0"
)

# Register paths
app.include_router(employee_routes.router, prefix="/employees", tags=["Employees"])

app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])