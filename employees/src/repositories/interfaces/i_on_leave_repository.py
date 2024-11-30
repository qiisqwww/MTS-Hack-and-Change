from abc import ABC, abstractmethod

from src.schemas import OnLeaveSchema

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
