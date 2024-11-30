from src.api.interfaces import IDepartmentsApi, IEmployeesAPI, IMLSearcherApi, IOrgStructureAPI


__all__ = [
    "SubServicesManagerService"
]


class SubServicesManagerService:
    _departments_api: IDepartmentsApi
    _employees_api: IEmployeesAPI
    _ml_searcher_api: IMLSearcherApi
    _org_structure_api: IOrgStructureAPI

    def __init__(
            self,
            departments_api: IDepartmentsApi,
            employees_api: IEmployeesAPI,
            ml_searcher_api: IMLSearcherApi,
            org_structure_api: IOrgStructureAPI
    ) -> None:
        self._departments_api = departments_api
        self._employees_api = employees_api
        self._ml_searcher_api = ml_searcher_api
        self._org_structure_api = org_structure_api

    async def get_info(self) -> list[dict]:
        departments = await self._departments_api.get_all_departments()
        posts_and_roles = await self._org_structure_api.get_all_posts_and_roles()

        return {
            "departaments": departments,
            "posts and roles": posts_and_roles
        }
