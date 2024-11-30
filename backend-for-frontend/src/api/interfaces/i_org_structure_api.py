from abc import ABC, abstractmethod

from src.schemas import PostSchema

__all__ = [
    "IOrgStructureAPI"
]


class IOrgStructureAPI(ABC):
    @abstractmethod
    async def find_post_and_role_by_name(self, post_id) -> PostSchema:
        ...

    @abstractmethod
    async def get_all_posts_and_roles(self) -> dict:
        ...
