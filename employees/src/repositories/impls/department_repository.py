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
        return [DepartmentSchema.from_orm(department) for department in await self._session.scalars(stmt)]

    async def get_department_by_name(self, department_name: str) -> DepartmentSchema:
        stmt = select(self._model).where(self._model.name == department_name)
        return DepartmentSchema.from_orm(await self._session.scalar(stmt))
