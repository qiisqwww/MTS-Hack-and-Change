from abc import ABC, abstractmethod

from src.schemas import PostSchema
from src.entities.models import Post

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

    @abstractmethod
    async def insert_prefill_posts(self, posts: list[Post]) -> None:
        ...
