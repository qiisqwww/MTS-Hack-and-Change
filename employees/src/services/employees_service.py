from src.repositories.interfaces import (
    IEmployeeRepository,
    IOnLeaveRepository,
    IOnSickLeaveRepository,
    IRoleRepository,
    IPostRepository,
    IDepartmentRepository
)
from src.schemas import EmployeeReturnSchema, EmployeeInputSchema, FilterSchema


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

    async def filter_employees_by_parameters(self) -> list[EmployeeReturnSchema]:
        ...
