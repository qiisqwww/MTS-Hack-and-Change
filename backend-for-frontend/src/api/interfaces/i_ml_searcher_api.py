from abc import ABC, abstractmethod

from src.schemas.employee_temp_schema import EmployeeTempSchema

__all__ = [
    "IMLSearcherApi"
]


class IMLSearcherApi(ABC):
    @abstractmethod
    async def filter_by_prompt(self, employees: list[EmployeeTempSchema], prompt: str) -> list[int]:
        ...
