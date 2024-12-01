from abc import ABC, abstractmethod

from src.schemas.employee_temp_schema import EmployeeTempSchema

__all__ = [
    "IMLSearcherApi"
]


class IMLSearcherApi(ABC):
    @abstractmethod
    async def filter_by_prompt(self, prompt: str, employees: list[EmployeeTempSchema]) -> list[int]:
        ...
