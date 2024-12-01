from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.repositories.repository import Repository
from src.repositories.interfaces import IOnLeaveRepository
from src.entities.models import OnLeave
from src.schemas import OnLeaveSchema

__all__ = [
    "OnLeaveRepository",
]


class OnLeaveRepository(Repository, IOnLeaveRepository):
    _model: type[OnLeave]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = OnLeave

    async def insert_on_leave(self, on_leave: OnLeaveSchema) -> OnLeaveSchema:
        pass

    async def get_on_leave(self, employee_id: int) -> OnLeaveSchema | None:
        stmt = select(self._model).where(self._model.employee_id == employee_id)
        on_leave = await self._session.scalar(stmt)

        if on_leave is None:
            return None

        return await OnLeaveSchema(
            date_from=on_leave.date_from,
            date_to=on_leave.date_to
        )

    async def insert_prefill_on_leaves(self, on_leaves: list[OnLeave]) -> None:
        self._session.add_all(on_leaves)
        await self._session.commit()
