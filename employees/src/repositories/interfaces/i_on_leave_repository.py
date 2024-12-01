from abc import ABC, abstractmethod

from src.schemas import OnLeaveSchema
from src.entities.models import OnLeave

__all__ = [
    "IOnLeaveRepository",
]


class IOnLeaveRepository(ABC):
    @abstractmethod
    async def insert_on_leave(self, on_leave: OnLeaveSchema) -> OnLeaveSchema:
        ...

    @abstractmethod
    async def get_on_leave(self, employee_id: int) -> OnLeaveSchema | None:
        ...

    @abstractmethod
    async def insert_prefill_on_leaves(self, on_leaves: list[OnLeave]) -> None:
        ...
