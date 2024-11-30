from fastapi import APIRouter

__all__ = [
    "filter_employees_router",
]


filter_employees_router = APIRouter()


@filter_employees_router.get("/filter")
async def filter_employees():
    ...
