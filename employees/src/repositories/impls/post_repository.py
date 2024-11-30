from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.repositories.repository import Repository
from src.repositories.interfaces import IPostRepository
from src.entities.models import Post
from src.schemas import PostSchema

__all__ = [
    "PostRepository",
]


class PostRepository(Repository, IPostRepository):
    _model: type[Post]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Post

    async def get_all_posts(self) -> list[PostSchema]:
        stmt = select(self._model)
        return [PostSchema.from_orm(post) for post in await self._session.scalars(stmt)]

    async def get_post_by_name(self, post_name: str) -> PostSchema | None:
        stmt = select(self._model).where(self._model.name == post_name)
        post = await self._session.scalar(stmt)

        if post is None:
            return None

        return PostSchema.from_orm(post)

    async def insert_prefill_posts(self, posts: list[Post]) -> None:
        self._session.add_all(posts)
        await self._session.commit()

    async def get_post_by_id(self, post_id: int) -> Post | None:
        stmt = select(self._model).where(self._model.id == post_id)

        return await self._session.scalar(stmt)
