from pydantic import BaseModel

from src.schemas.role_schema import RoleSchema

__all__ = [
    "PostSchema"
]


class PostSchema(BaseModel):
    id: int
    name: str
    role: RoleSchema
