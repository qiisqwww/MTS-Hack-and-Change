from abc import ABC, abstractmethod

from src.schemas import DepartmentSchema

__all__ = [
    "IDepartmentRepository",
]


class IDepartmentRepository(ABC):
    @abstractmethod
    async def get_all_departments(self) -> list[DepartmentSchema]:
        ...

    @abstractmethod
    async def get_department_by_name(self, department_name: str) -> DepartmentSchema:
        ...
