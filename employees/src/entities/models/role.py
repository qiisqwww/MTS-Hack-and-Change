from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "Role"
]


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)

    posts = relationship("Post", back_populates='role', lazy='selectin')
