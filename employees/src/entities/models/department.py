from sqlalchemy import Column, Integer, String

from src.entities.declarative_base import Base

__all__ = [
    "Department",
]


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    path = Column(String)
