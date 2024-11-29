from sqlalchemy import Column, Integer, Date, ForeignKey

from src.entities.declarative_base import Base

__all__ = [
    "OnSickLeave"
]


class OnSickLeave(Base):
    __tablename__ = 'on_leaves'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
