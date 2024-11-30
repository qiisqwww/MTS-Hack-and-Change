from abc import ABC, abstractmethod

from src.schemas import PostSchema

__all__ = [
    "IPostRepository",
]


class IPostRepository(ABC):
    @abstractmethod
    async def get_all_posts(self) -> list[PostSchema]:
        ...

    @abstractmethod
    async def get_post_by_name(self, post_name: str) -> PostSchema:
        ...