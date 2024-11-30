from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "OnLeave"
]


class OnLeave(Base):
    __tablename__ = 'on_sick_leaves'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)

    employee = relationship("Employee", back_populates="leaves", uselist=False)
