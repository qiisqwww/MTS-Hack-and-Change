from typing import List

from src.repositories.interfaces import (
    IEmployeeRepository,
    IOnLeaveRepository,
    IOnSickLeaveRepository,
    IRoleRepository,
    IPostRepository,
    IDepartmentRepository
)
from src.schemas import (
    EmployeeReturnSchema,
    EmployeeInputSchema,
    FiltersSchema,
    FiltersQuerySchema,
    OnLeaveSchema,
    OnSickLeaveSchema
)


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

        employees = await self._employee_repository.get_employee_by_filters(filters_for_query)

        employees_schema = []
        for employee in employees:
            on_sick_leave, on_leave = None, None
            if employee.sick_leaves is not None:
                on_sick_leave = OnSickLeaveSchema(
                    date_from=employee.sick_leaves.date_from,
                    date_to=employee.sick_leaves.date_to
                )

            if employee.leaves is not None:
                on_leave = OnLeaveSchema(
                    date_from=employee.leaves.date_from,
                    date_to=employee.leaves.date_to
                )

            employees_schema.append(EmployeeReturnSchema(
                id=employee.id,
                post=employee.post.name,
                department_path=employee.department.path,
                department_name=employee.department.name,
                role=employee.post.role.name,
                first_name=employee.first_name,
                last_name=employee.last_name,
                birthdate=employee.birthdate,
                sex=employee.sex,
                phone_number=employee.phone_number,
                city=employee.city,
                address=employee.address,
                tg_username=employee.tg_username,
                email=employee.email,
                on_sick_leave_info=on_sick_leave,
                on_leave_info=on_leave,
                boss_id=employee.boss_id,
                about=employee.about
            ))

        return employees_schema

    async def find_employee_by_id(self, employee_id: int) -> EmployeeReturnSchema | None:
        employee = await self._employee_repository.get_employee_by_id(employee_id)

        if employee is None:
            return None

        employee_post = await self._post_repository.get_post_by_id(employee.post_id)
        employee_role = await self._role_repository.get_role_by_id(employee_post.role_id)
        employee_department = await self._department_repository.get_department_by_id(employee.department_id)
        on_sick_leave = await self._on_sick_leave_repository.get_on_sick_leave(employee.id)
        on_leave = await self._on_leave_repository.get_on_leave(employee.id)

        return EmployeeReturnSchema(
            id=employee.id,
            post=employee_post.name,
            department_path=employee_department.path,
            department_name=employee_department.name,
            role=employee_role.name,
            first_name=employee.first_name,
            last_name=employee.last_name,
            birthdate=employee.birthdate,
            sex=employee.sex,
            phone_number=employee.phone_number,
            city=employee.city,
            address=employee.address,
            tg_username=employee.tg_username,
            email=employee.email,
            on_sick_leave_info=on_sick_leave,
            on_leave_info=on_leave,
            boss_id=employee.boss_id,
            about=employee.about
        )

    async def find_subs_by_employee_id(self, employee_id: int) -> List[EmployeeReturnSchema] | None:
        boss = await self._employee_repository.get_employee_by_id(employee_id)
        if boss is None:
            return None

        subs = await self._employee_repository.find_employee_subs_by_id(employee_id)

        print(subs)

        subs_schema = []
        for sub in subs:
            on_sick_leave, on_leave = None, None
            if sub.sick_leaves is not None:
                on_sick_leave = OnSickLeaveSchema(
                    date_from=sub.sick_leaves.date_from,
                    date_to=sub.sick_leaves.date_to
                )

            if sub.leaves is not None:
                on_leave = OnLeaveSchema(
                    date_from=sub.leaves.date_from,
                    date_to=sub.leaves.date_to
                )

            subs_schema.append(EmployeeReturnSchema(
                id=sub.id,
                post=sub.post.name,
                department_path=sub.department.path,
                department_name=sub.department.name,
                role=sub.post.role.name,
                first_name=sub.first_name,
                last_name=sub.last_name,
                birthdate=sub.birthdate,
                sex=sub.sex,
                phone_number=sub.phone_number,
                city=sub.city,
                address=sub.address,
                tg_username=sub.tg_username,
                email=sub.email,
                on_sick_leave_info=on_sick_leave,
                on_leave_info=on_leave,
                boss_id=sub.boss_id,
                about=sub.about
            ))

        return subs_schema
