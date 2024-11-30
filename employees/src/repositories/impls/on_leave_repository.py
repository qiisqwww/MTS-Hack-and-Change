from sqlalchemy.ext.asyncio import AsyncSession

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
        pass
