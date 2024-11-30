from abc import ABC, abstractmethod

from src.schemas import EmployeeSchema, FiltersQuerySchema
from src.entities.models import Employee

__all__ = [
    "IEmployeeRepository",
]


class IEmployeeRepository(ABC):
    @abstractmethod
    async def get_employee_by_id(self, employee_id: int) -> Employee | None:
        ...

    @abstractmethod
    async def get_employee_by_filters(self, filters: FiltersQuerySchema) -> list[Employee]:
        ...

    @abstractmethod
    async def insert_prefill_employees(self, employees: Employee) -> None:
        ...
