from sqlalchemy.orm import Session
from app.models.employee_model import Employee

#Fetches all employee records from the database. Returns a list of Employee objects
def get_all_employees(db: Session):
    return db.query(Employee).all()

#Adds a new employee to the database using the provided details in employee_data.
# Returns the newly created Employee object after committing to the database
def create_employee(db: Session, employee_data):
    new_employee = Employee(**employee_data)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


#Removes an employee from the database by their ID.
# Returns the deleted Employee object if found;
# otherwise, returns None
def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee