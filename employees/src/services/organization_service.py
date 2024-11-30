from src.repositories.interfaces import IRoleRepository, IDepartmentRepository, IPostRepository

from src.schemas import DepartmentSchema, RoleSchema


__all__ = [
    "OrganizationService",
]


class OrganizationService:
    _department_repository: IDepartmentRepository
    _role_repository: IRoleRepository
    _post_repository: IPostRepository

    def __init__(
            self,
            department_repository: IDepartmentRepository,
            role_repository: IRoleRepository,
            post_repository: IPostRepository
    ) -> None:
        self._department_repository = department_repository
        self._role_repository = role_repository
        self._post_repository = post_repository

    async def get_all(self):
        posts = await self._post_repository.get_all_posts()
        roles = await self._role_repository.get_all_roles()
        departments = await self._department_repository.get_all_departments()

        return {
            "departments": departments,
            "posts_and_roles": {
                "posts": posts,
                "roles": roles
            }
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
