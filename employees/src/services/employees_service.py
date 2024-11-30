from src.repositories.interfaces import (
    IEmployeeRepository,
    IOnLeaveRepository,
    IOnSickLeaveRepository,
    IRoleRepository,
    IPostRepository,
    IDepartmentRepository
)
from src.schemas import EmployeeReturnSchema, EmployeeInputSchema, FiltersSchema, FiltersQuerySchema


class EmployeesService:
    _employee_repository: IEmployeeRepository
    _on_leave_repository: IOnLeaveRepository
    _on_sick_leave_repository: IOnSickLeaveRepository
    _role_repository: IRoleRepository
    _post_repository: IPostRepository
    _department_repository: IDepartmentRepository

    def __init__(
            self,
            employee_repository: IEmployeeRepository,
            on_leave_repository: IOnLeaveRepository,
            on_sick_leave_repository: IOnSickLeaveRepository,
            role_repository: IRoleRepository,
            post_repository: IPostRepository,
            department_repository: IDepartmentRepository
    ) -> None:
        self._employee_repository = employee_repository
        self._on_leave_repository = on_leave_repository
        self._on_sick_leave_repository = on_sick_leave_repository
        self._role_repository = role_repository
        self._post_repository = post_repository
        self._department_repository = department_repository

    async def add_new_employee(self, employee_input: EmployeeInputSchema) -> EmployeeReturnSchema:
        ...

    async def filter_employees_by_parameters(self, filters: FiltersSchema) -> list[EmployeeReturnSchema]:
        role, post, department = None, None, None

        if filters.role:
            role = await self._role_repository.get_role_by_name(filters.role)
        if filters.post:
            post = await self._post_repository.get_post_by_name(filters.post)
        if filters.department_name:
            department = await self._department_repository.get_department_by_name(filters.department_name)

        filters_for_query = FiltersQuerySchema(
            department_id=department.id if department else None,
            post_id=post.id if post else None,
            role_id=role.id if role else None,
            first_name=filters.first_name,
            last_name=filters.last_name,
            phone_number=filters.phone_number,
            city=filters.city,
            address=filters.address,
            email=filters.email,
            tg_username=filters.tg_username
        )
