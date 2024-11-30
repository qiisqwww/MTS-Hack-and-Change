from aiohttp import ClientSession

from src.api.interfaces import IOrgStructureAPI
from src.schemas import PostSchema

__all__ = [
    "OrgStructureAPI"
]


class OrgStructureAPI(IOrgStructureAPI):
    _ORG_STRUCTURE_URL = "http://org-structure:8084"

    async def find_post_and_role_by_name(self, post_id) -> PostSchema:
        ...

    async def get_all_posts_and_roles(self) -> dict:
        async with ClientSession() as session:
            try:
                response = await session.get(url=self._ORG_STRUCTURE_URL+"/api/all")
            except Exception:
                return {}

            if response.status != 200:
                return {}

            posts_and_roles = await response.json(encoding="utf-8")
            return posts_and_roles
