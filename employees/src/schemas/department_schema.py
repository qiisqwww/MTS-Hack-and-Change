from pydantic import BaseModel, ConfigDict

__all__ = [
    "DepartmentSchema",
]


class DepartmentSchema(BaseModel):
    id: int
    name: int
    path: str

    model_config = ConfigDict(from_attributes=True)
