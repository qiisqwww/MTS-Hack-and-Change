from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "Employee"
]


class  Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    birthdate = Column(Date)
    sex = Column(String)
    phone_number = Column(String(length=20), nullable=False)
    email = Column(String(length=100), nullable=False)
    tg_username = Column(String(length=100))
    city = Column(String, nullable=False)
    address = Column(String)
    boss_id = Column(Integer, ForeignKey('employees.id'))
    about = Column(String, nullable=False, default="")

    post = relationship("Post", back_populates="employees", lazy='selectin')
    department = relationship("Department", back_populates="employees", lazy='selectin')
    sick_leaves = relationship(
        "OnSickLeave",
        back_populates="employee",
        cascade="all, delete-orphan",
        uselist=False,
        lazy='selectin'
    )
    leaves = relationship(
        "OnLeave",
        back_populates="employee",
        cascade="all, delete-orphan",
        uselist=False,
        lazy='selectin'
    )
