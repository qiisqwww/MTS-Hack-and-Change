from pydantic import BaseModel

__all__ = [
    "RoleSchema"
]


class RoleSchema(BaseModel):
    id: int
    name: str
