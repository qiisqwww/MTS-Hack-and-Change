from sqlalchemy import Column, Integer, String

from src.entities.declarative_base import Base

__all__ = [
    "FunctionalBlock",
]


class FunctionalBlock(Base):
    __tablename__ = 'functional_blocks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)

