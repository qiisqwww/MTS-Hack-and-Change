from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.repositories.impls import (
    EmployeeRepository,
    OnLeaveRepository,
    OnSickLeaveRepository,
    RoleRepository,
    PostRepository,
    DepartmentRepository
)
from src.services import EmployeesService, OrganizationService
from src.database import get_async_session

__all__ = [
    "get_employees_info_service",
    "get_organization_service"
]


async def get_employees_info_service(session: AsyncSession = Depends(get_async_session)) -> EmployeesService:
    return EmployeesService(
        EmployeeRepository(session),
        OnLeaveRepository(session),
        OnSickLeaveRepository(session),
        RoleRepository(session),
        PostRepository(session),
        DepartmentRepository(session)
    )


async def get_organization_service(session: AsyncSession = Depends(get_async_session)) -> OrganizationService:
    return OrganizationService(
        DepartmentRepository(session),
        RoleRepository(session),
        PostRepository(session)
    )
