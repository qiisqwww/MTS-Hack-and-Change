from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.repositories.impls import EmployeeRepository, OnLeaveRepository, OnSickLeaveRepository
from src.services import EmployeesInfoService
from src.database import get_async_session

__all__ = [
    "get_employees_info_service"
]


async def get_employees_info_service(session: AsyncSession = Depends(get_async_session)) -> EmployeesInfoService:
    return EmployeesInfoService(
        EmployeeRepository(session),
        OnLeaveRepository(session),
        OnSickLeaveRepository(session)
    )
