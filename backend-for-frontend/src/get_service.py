from src.services import SubServicesManagerService
from src.api.impls import DepartmentsApi, EmployeesAPI, MLSearcherApi, OrgStructureAPI

__all__ = [
    "get_sub_services_manager_service",
]


async def get_sub_services_manager_service() -> SubServicesManagerService:
    return SubServicesManagerService(
        DepartmentsApi(),
        EmployeesAPI(),
        MLSearcherApi(),
        OrgStructureAPI()
    )
