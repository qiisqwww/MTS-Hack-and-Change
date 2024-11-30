from src.repositories.interfaces import IDepartamentRepository

from src.schemas import DepartmentSchema


__all__ = [
    "DepartmentService",
]


class DepartmentService:
    _department_repository: IDepartamentRepository

    def __init__(self, department_repository: IDepartamentRepository) -> None:
        self._department_repository = department_repository

    async def get_all_departments(self) -> list[DepartmentSchema]:
        departments = await self._department_repository.get_all_departments()

        return departments
