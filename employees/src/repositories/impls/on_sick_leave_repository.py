from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.repositories.repository import Repository
from src.repositories.interfaces import IOnSickLeaveRepository
from src.entities.models import OnSickLeave
from src.schemas import OnSickLeaveSchema

__all__ = [
    "OnSickLeaveRepository",
]


class OnSickLeaveRepository(Repository, IOnSickLeaveRepository):
    _model: type[OnSickLeave]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = OnSickLeave

    async def insert_on_sick_leave(self, on_sick_leave: OnSickLeaveSchema) -> OnSickLeaveSchema:
        pass

    async def get_on_sick_leave(self, employee_id: int) -> OnSickLeaveSchema | None:
        stmt = select(self._model).where(self._model.employee_id == employee_id)
        on_sick_leave = await self._session.scalar(stmt)

        if on_sick_leave is None:
            return None

        return await OnSickLeaveSchema(
            date_from=on_sick_leave.date_from,
            date_to=on_sick_leave.date_to
        )
