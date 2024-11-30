from aiohttp import ClientSession

from src.api.interfaces import IDepartmentsApi
from src.schemas import DepartmentSchema

__all__ = [
    "DepartmentsApi",
]


class DepartmentsApi(IDepartmentsApi):
    _DEPARTMENTS_URL = "http://departments:8082"

    async def find_department_by_name(self, department_name: str) -> list[DepartmentSchema]:
        pass

    async def get_all_departments(self) -> dict:
        async with ClientSession() as session:
            try:
                response = await session.get(url=self._DEPARTMENTS_URL+"/api/all")
            except Exception as e:
                print(e)
                return {}

            if response.status != 200:
                print("NON 200")
                return {}

            departments = await response.json(encoding="utf-8")
            return departments
