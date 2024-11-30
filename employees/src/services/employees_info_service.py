from src.repositories.interfaces import (
    IEmployeeRepository,
    IOnLeaveRepository,
    IOnSickLeaveRepository
)
from src.schemas import EmployeeReturnSchema, EmployeeInputSchema


class EmployeesInfoService:
    _employee_repository: IEmployeeRepository
    _on_leave_repository: IOnLeaveRepository
    _on_sick_leave_repository: IOnSickLeaveRepository

    def __init__(
            self,
            employee_repository: IEmployeeRepository,
            on_leave_repository: IOnLeaveRepository,
            on_sick_leave_repository: IOnSickLeaveRepository
    ) -> None:
        self._employee_repository = employee_repository
        self._on_leave_repository = on_leave_repository
        self._on_sick_leave_repository = on_sick_leave_repository

    async def add_new_employee(self, employee_input: EmployeeInputSchema) -> EmployeeReturnSchema:
        ...

    async def filter_employees_by_parameters(self) -> list[EmployeeReturnSchema]:
        ...
