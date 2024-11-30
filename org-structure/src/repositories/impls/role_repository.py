from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.repositories.repository import Repository
from src.repositories.interfaces import IRoleRepository
from src.entities.models import Role
from src.schemas import RoleSchema

__all__ = [
    "RoleRepository",
]


class RoleRepository(Repository, IRoleRepository):
    _model: type[Role]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Role

    async def get_all_roles(self) -> list[RoleSchema]:
        stmt = select(self._model)
        return [RoleSchema.from_orm(role) for role in await self._session.scalars(stmt)]

    async def get_role_by_id(self, role_id: int) -> RoleSchema | None:
        stmt = select(self._model).where(self._model.id == role_id)
        role = await self._session.scalar(stmt)

        if role is None:
            return None

        return RoleSchema.from_orm(role)

    async def get_role_by_name(self, role_name: str) -> RoleSchema | None:
        stmt = select(self._model).where(self._model.name == role_name)
        role = await self._session.scalar(stmt)

        if role is None:
            return None

        return RoleSchema.from_orm(role)
