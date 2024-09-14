from pydantic import BaseModel, Field, validator
from typing import Optional

class TaskSchema(BaseModel):
    task_name: str = Field(..., max_length=100)  # Se asegura que el nombre de la tarea no supere los 100 caracteres
    status: str = Field(..., max_length=20)  # Se asegura que el estado no supere los 20 caracteres
    employee_id: Optional[int] = Field(None, gt=0)  # El ID del empleado debe ser un entero positivo

    model_config = {
        'from_attribute': True
    }


class TaskDto(TaskSchema):
    pass






