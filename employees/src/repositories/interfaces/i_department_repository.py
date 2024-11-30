from abc import ABC, abstractmethod

from src.schemas import DepartmentSchema

__all__ = [
    "IDepartmentRepository",
]


class IDepartmentRepository(ABC):
    @abstractmethod
    async def get_all_departments(self) -> list[DepartmentSchema]:
        ...
