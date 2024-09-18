from fastapi.params import Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.config.config import get_db
from app.repositories import employee_repository
from app.services.secutiry import SECRET_KEY, ALGORITHM
from fastapi import HTTPException


async def get_current_user(token: str, db: Session=Depends(get_db())):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate credentials')

    employee = employee_repository.get_employee_by_email(db, email)

    if employee is None:
        raise HTTPException(status_code=404, detail='employee has not found')

    return employee