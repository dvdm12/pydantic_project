from sqlalchemy import Integer, Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.config.config import Base


class ProductORM(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Integer)
    expiration_date = Column(Date, nullable=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))

    employee = relationship("Employee", back_populates="products")