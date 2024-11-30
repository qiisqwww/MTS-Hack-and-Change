from aiohttp import ClientSession

from src.api.interfaces import IEmployeesAPI
from src.schemas import EmployeesFiltersSchema

__all__ = [
    "EmployeesAPI",
]


class EmployeesAPI(IEmployeesAPI):
    _EMPLOYEES_URL = "http://employees:8082"

    async def find_employees_by_filters(self, filters: EmployeesFiltersSchema) -> list[int]:
        pass

    async def get_all_data(self) -> dict:
        async with ClientSession() as session:
            try:
                response = await session.get(url=self._EMPLOYEES_URL + "/api/all")
            except Exception:
                return {}

            if response.status != 200:
                return {}

            all_data = await response.json(encoding="utf-8")

        return all_data
