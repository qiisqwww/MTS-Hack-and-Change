from abc import ABC, abstractmethod

from src.schemas import RoleSchema
from src.entities.models import Role

__all__ = [
    "IRoleRepository",
]


class IRoleRepository(ABC):
    @abstractmethod
    async def get_all_roles(self) -> list[RoleSchema]:
        ...

    @abstractmethod
    async def get_role_by_id(self, role_id: int) -> RoleSchema:
        ...

    @abstractmethod
    async def get_role_by_name(self, role_name: str) -> RoleSchema:
        ...

    @abstractmethod
    async def insert_prefill_roles(self, roles: list[Role]) -> None:
        ...
