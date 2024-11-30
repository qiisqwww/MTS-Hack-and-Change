from src.api.interfaces import IEmployeesAPI
from src.schemas import EmployeesFiltersSchema

__all__ = [
    "EmployeesAPI",
]


class EmployeesAPI(IEmployeesAPI):
    _EMPLOYEES_URL = "http://employees:8083"

    async def find_employees_by_filters(self, filters: EmployeesFiltersSchema) -> list[int]:
        pass
