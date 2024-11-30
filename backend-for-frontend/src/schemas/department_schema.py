from pydantic import BaseModel

__all__ = [
    "DepartmentSchema"
]


class DepartmentSchema(BaseModel):
    id: int
    name: str
    parent_department_id: int
