from abc import ABC, abstractmethod
from typing import List

from src.schemas import FiltersSchema

__all__ = [
    "IEmployeesAPI"
]


class IEmployeesAPI(ABC):
    @abstractmethod
    async def find_employees_by_filters(self, filters: FiltersSchema) -> list[int]:
        ...

    @abstractmethod
    async def get_all_data(self) -> dict:
        ...

    @abstractmethod
    async def find_employee_by_id(self, boss_id: int) -> dict:
        ...

    @abstractmethod
    async def find_employee_subs(self, boss_id: int) -> List[dict]:
        ...
