from abc import ABC, abstractmethod

from src.schemas import DepartmentSchema

__all__ = [
    "IDepartamentRepository",
]


class IDepartamentRepository(ABC):
    @abstractmethod
    async def get_all_departments(self) -> list[DepartmentSchema]:
        ...
