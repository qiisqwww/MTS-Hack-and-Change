from abc import ABC, abstractmethod

from src.schemas import EmployeeSchema

__all__ = [
    "IEmployeeRepository",
]


class IEmployeeRepository(ABC):
    @abstractmethod
    async def insert_employee(self, employee: EmployeeSchema) -> EmployeeSchema:
        ...

    @abstractmethod
    async def get_employee_by_id(self, employee_id: int) -> EmployeeSchema | None:
        ...
