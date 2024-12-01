from aiohttp import ClientSession

from src.api.interfaces import IEmployeesAPI
from src.schemas import FiltersSchema

__all__ = [
    "EmployeesAPI",
]


class EmployeesAPI(IEmployeesAPI):
    _EMPLOYEES_URL = "http://employees:8082"

    async def find_employees_by_filters(self, filters: FiltersSchema) -> list[int]:
        async with ClientSession() as session:
            try:
                response = await session.post(
                    url=self._EMPLOYEES_URL + "/api/filter",
                    json=filters.dict()
                )
            except Exception:
                return {}

            if response.status != 200:
                return {}

            filtered_employees = await response.json(encoding="utf-8")

        return filtered_employees

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

    async def find_employee_by_id(self, boss_id: int) -> dict:
        async with ClientSession() as session:
            try:
                response = await session.get(url=self._EMPLOYEES_URL + f"/api/employee?employee_id={boss_id}")
            except Exception:
                return {}

            if response.status != 200:
                return {}

            employee = await response.json(encoding="utf-8")

        return employee
