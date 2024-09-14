from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    first_name: str = Field(..., max_length=20)
    last_name: str = Field(..., max_length=20)
    email: EmailStr = Field(..., max_length=50)

    model_config = {
        'from_attributes': True
    }


class EmployeeDto(EmployeeBase):
    pass

