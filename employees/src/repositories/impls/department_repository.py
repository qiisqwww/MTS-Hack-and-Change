from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.repositories.repository import Repository
from src.repositories.interfaces import IDepartmentRepository
from src.schemas import DepartmentSchema
from src.entities.models import Department

__all__ = [
    "DepartmentRepository",
]


class DepartmentRepository(Repository, IDepartmentRepository):
    _model: type[Department]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Department

    async def get_all_departments(self) -> list[DepartmentSchema]:
        stmt = select(self._model)
        return [DepartmentSchema.from_orm(department)
                for department in await self._session.scalars(stmt) if department is not None]

    async def get_department_by_name(self, department_name: str) -> DepartmentSchema | None:
        stmt = select(self._model).where(self._model.name == department_name)
        department = await self._session.scalar(stmt)

        return DepartmentSchema.from_orm(department) if department is not None else None

    async def insert_prefill_departments(self, departments: list[Department]) -> None:
        self._session.add_all(departments)
        await self._session.commit()
