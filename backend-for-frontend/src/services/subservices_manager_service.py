from src.api.interfaces import IEmployeesAPI, IMLSearcherApi
from src.schemas import FiltersSchema


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

    async def filter_employees(self, filters: FiltersSchema, prompt: str | None) -> dict:
        filtered_employees = await self._employees_api.find_employees_by_filters(filters)

        if prompt is not None:
            pass

        return filtered_employees
