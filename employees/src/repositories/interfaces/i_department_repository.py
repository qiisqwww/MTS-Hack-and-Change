from abc import ABC, abstractmethod

from src.schemas import DepartmentSchema
from src.entities.models import Department

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

    @abstractmethod
    async def insert_prefill_departments(self, departments: list[Department]) -> None:
        ...

    @abstractmethod
    async def get_department_by_id(self, department_id: int) -> Department:
        ...
