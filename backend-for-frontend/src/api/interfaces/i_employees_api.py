from abc import ABC, abstractmethod

from src.schemas import EmployeesFiltersSchema

__all__ = [
    "IEmployeesAPI"
]


class IEmployeesAPI(ABC):
    @abstractmethod
    async def find_employees_by_filters(self, filters: EmployeesFiltersSchema) -> list[int]:  # [post_id, role_id]
        ...
