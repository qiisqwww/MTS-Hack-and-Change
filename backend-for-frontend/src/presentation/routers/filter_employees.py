from fastapi import APIRouter

__all__ = [
    "filter_employees",
]


filter_employees_router = APIRouter()
@filter_employees_router.get("/by-filters")
async def filter_employees():
    ...
