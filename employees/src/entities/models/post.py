from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "Post"
]


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    role = relationship("Role", back_populates="posts")
