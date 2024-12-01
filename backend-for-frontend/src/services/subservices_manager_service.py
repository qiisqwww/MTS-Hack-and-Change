from src.api.interfaces import IEmployeesAPI, IMLSearcherApi
from src.schemas import FiltersSchema, EmployeeTempSchema


__all__ = [
    "SubServicesManagerService"
]


class SubServicesManagerService:
    _employees_api: IEmployeesAPI
    _ml_searcher_api: IMLSearcherApi

    def __init__(self, employees_api: IEmployeesAPI, ml_searcher_api: IMLSearcherApi) -> None:
        self._employees_api = employees_api
        self._ml_searcher_api = ml_searcher_api

    async def get_info(self) -> list[dict]:
        all_data = await self._employees_api.get_all_data()

        return all_data

    async def filter_employees(self, filters: FiltersSchema, prompt: str | None) -> list[EmployeeTempSchema]:
        filtered_employees_raw = await self._employees_api.find_employees_by_filters(filters)

        filtered_employees = [EmployeeTempSchema(**emp) for emp in filtered_employees_raw["filtered_employees"]]

        if prompt is not None:
            matching_ids = set(await self._ml_searcher_api.filter_by_prompt(prompt, filtered_employees))

            filtered_employees_from_ml = []
            for emp in filtered_employees:
                if emp.id in matching_ids:
                    filtered_employees_from_ml.append(emp)

            filtered_employees = filtered_employees_from_ml


        return filtered_employees

    async def find_employee_boss(self, boss_id: int) -> EmployeeTempSchema:
        boss = await self._employees_api.find_employee_by_id(boss_id)

        return EmployeeTempSchema(**boss)
