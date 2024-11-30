from abc import ABC, abstractmethod

from src.schemas.on_sick_leave_schema import OnSickLeaveSchema

__all__ = [
    "IOnSickLeaveRepository"
]


class IOnSickLeaveRepository(ABC):
    @abstractmethod
    async def insert_on_sick_leave(self, on_sick_leave: OnSickLeaveSchema) -> OnSickLeaveSchema:
        ...

    @abstractmethod
    async def get_on_sick_leave(self, employee_id: int) -> OnSickLeaveSchema | None:
        ...
