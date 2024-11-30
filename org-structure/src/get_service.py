from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.services import PostsAndRolesService
from src.database import get_async_session
from src.repositories.impls import RoleRepository, PostRepository

__all__ = [
    "get_posts_and_roles_service",
]


async def get_posts_and_roles_service(session: AsyncSession = Depends(get_async_session)) -> PostsAndRolesService:
    return PostsAndRolesService(
        PostRepository(session),
        RoleRepository(session),
    )
