from sqlalchemy import Column, String, Integer, Date, Boolean

from src.entities.declarative_base import Base

__all__ = [
    "Employee"
]


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    post_id = Column(Integer, nullable=False)
    functional_blocks_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)
    first_name = Column(String(length=100), nullable=False)
    middle_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    birthdate = Column(Date, nullable=False)
    sex = Column(String, nullable=False)
    phone_number = Column(String(length=12), nullable=False)
    email = Column(String(length=100), nullable=False)
    tg_username = Column(String(length=100))
    city = Column(String, nullable=False)
    address = Column(String)
    is_on_sick_leave = Column(Boolean, nullable=False, default=False)
    is_on_leave = Column(Boolean, nullable=False, default=False)
