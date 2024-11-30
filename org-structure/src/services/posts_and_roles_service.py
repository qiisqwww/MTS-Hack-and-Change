from src.repositories.interfaces import IPostRepository, IRoleRepository
from src.schemas import PostSchema, RoleSchema


class PostsAndRolesService:
    _post_repository: IPostRepository
    _role_repository: IRoleRepository

    def __init__(self, post_repository: IPostRepository, role_repository: IRoleRepository) -> None:
        self._post_repository = post_repository
        self._role_repository = role_repository

    async def get_all_posts_and_roles(self):
        posts = await self._post_repository.get_all_posts()
        roles = await self._role_repository.get_all_roles()

        return {
            "posts": posts,
            "roles": roles
        }

    async def get_post_and_role_by_post_name(self, post_name: str) -> dict:
        post = await self._post_repository.get_post_by_name(post_name)

        if post is None:
            return None

        role = await self._role_repository.get_role_by_id(post.role_id)
        return {
            "post": post,
            "role": role
        }

    async def get_role_by_name(self, role_name: str) -> RoleSchema:
        role = await self._role_repository.get_role_by_name(role_name)

        if role is None:
            return None

        return {"role": role}
