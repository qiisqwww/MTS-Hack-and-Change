from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.repository import Repository
from src.repositories.interfaces import IEmployeeRepository
from src.entities.models import Employee
from src.schemas import EmployeeSchema, EmployeeInputSchema

__all__ = [
    "EmployeeRepository"
]


class EmployeeRepository(Repository, IEmployeeRepository):
    _model: type[Employee]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Employee

    async def insert_employee(self, employee: EmployeeInputSchema) -> EmployeeSchema:
        pass

    async def get_employee_by_id(self, employee_id: int) -> EmployeeSchema | None:
        pass
