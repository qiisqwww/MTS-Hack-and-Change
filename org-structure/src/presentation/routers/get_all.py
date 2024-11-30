from fastapi import APIRouter, Depends

from src.get_service import get_posts_and_roles_service
from src.services import PostsAndRolesService

__all__ = [
    "get_all_router"
]


get_all_router = APIRouter()


@get_all_router.get("/all")
async def get_all(posts_and_roles_service: PostsAndRolesService = Depends(get_posts_and_roles_service)):
    return await posts_and_roles_service.get_all_posts_and_roles()
