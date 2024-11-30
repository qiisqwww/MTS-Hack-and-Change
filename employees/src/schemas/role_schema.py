from pydantic import BaseModel, ConfigDict

__all__ = [
    "RoleSchema"
]


class RoleSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
