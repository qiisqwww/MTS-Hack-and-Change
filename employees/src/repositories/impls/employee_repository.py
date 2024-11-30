from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_

from src.repositories.repository import Repository
from src.repositories.interfaces import IEmployeeRepository
from src.entities.models import Employee
from src.schemas import FiltersQuerySchema
from src.entities.models import Post, OnLeave, OnSickLeave

__all__ = [
    "EmployeeRepository"
]


class EmployeeRepository(Repository, IEmployeeRepository):
    _model: type[Employee]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Employee

    async def get_employee_by_id(self, employee_id: int) -> Employee | None:
        pass

    async def get_employee_by_filters(self, filters: FiltersQuerySchema) -> list[Employee]:
        stmt = (
            select(self._model)
            .join(self._model.post)
            .join(Post.role)
            .join(self._model.department)
            .outerjoin(OnLeave, OnLeave.employee_id == self._model.id)
            .outerjoin(OnSickLeave, OnSickLeave.employee_id == self._model.id)
        )

        conditions = []
        if filters.post_id:
            conditions.append(self._model.post_id == filters.post_id)
        if filters.role_id:
            conditions.append(Post.role_id == filters.role_id)
        if filters.department_id:
            conditions.append(self._model.department_id == filters.department_id)

        for field, value in filters.dict().items():
            if field in ('post_id', 'role_id', 'department_id'):
                continue

            if value is not None:
                conditions.append(getattr(self._model, field) == value)
                print(field, value)

        if conditions:
            stmt = stmt.where(and_(*conditions))

        result = await self._session.execute(stmt)
        employees = result.scalars().all()

        return employees

    async def insert_prefill_employees(self, employees: Employee) -> None:
        self._session.add_all(employees)
        await self._session.commit()
