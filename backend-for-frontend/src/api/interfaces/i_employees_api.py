from abc import ABC, abstractmethod

from src.schemas import EmployeesFiltersSchema

__all__ = [
    "IEmployeesAPI"
]


class IEmployeesAPI(ABC):
    @abstractmethod
    async def find_employees_by_filters(self, filters: EmployeesFiltersSchema) -> list[int]:
        ...

    @abstractmethod
    async def get_all_data(self) -> dict:
        ...