from abc import ABC, abstractmethod

from src.schemas import DepartmentSchema

__all__ = [
    "IDepartmentsApi"
]


class IDepartmentsApi(ABC):
    @abstractmethod
    async def find_department_by_name(self, department_name: str) -> list[DepartmentSchema]:
        ...

    @abstractmethod
    async def get_all_departments(self) -> dict:
        ...
