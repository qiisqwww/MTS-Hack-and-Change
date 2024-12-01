import json
from datetime import datetime

from src.repositories.impls import (
    RoleRepository,
    PostRepository,
    DepartmentRepository,
    EmployeeRepository,
    OnLeaveRepository,
    OnSickLeaveRepository
)
from src.entities.models import Role, Post, Employee, Department, OnLeave, OnSickLeave
from src.database import async_session_maker

__all__ = [
    "prefill_database"
]


async def prefill_database() -> None:
    async with async_session_maker() as session:

        if await db_already_filled(RoleRepository(session)):
            return

        await prefill_roles(RoleRepository(session))
        await prefill_posts(PostRepository(session))
        await prefill_departments(DepartmentRepository(session))
        await prefill_employees(EmployeeRepository(session))
        await prefill_on_leaves(OnLeaveRepository(session))
        await prefill_on_sick_leaves(OnSickLeaveRepository(session))


async def db_already_filled(role_repository: RoleRepository) -> bool:
    return len(await role_repository.get_all_roles()) != 0


async def prefill_roles(role_repository: RoleRepository) -> None:
    roles = []
    with open("/app/prefill/roles.json", "r") as file:
        roles_data = json.load(file)
        for role in roles_data:
            roles.append(Role(id=int(role["id"]), name=role["role"]))

    await role_repository.insert_prefill_roles(roles)


async def prefill_posts(post_repository: PostRepository) -> None:
    posts = []
    with open("/app/prefill/posts.json", "r") as file:
        posts_data = json.load(file)
        for post in posts_data:
            posts.append(Post(id=int(post["id"]), name=post["name"], role_id=int(post["role_id"])))

    await post_repository.insert_prefill_posts(posts)


async def prefill_departments(department_repository: DepartmentRepository) -> None:
    departments = []
    with open("/app/prefill/departments.json", "r") as file:
        departments_data = json.load(file)
        for dep in departments_data:
            departments.append(Department(id=int(dep["id"]), name=dep["name"], path=dep["path"]))

    await department_repository.insert_prefill_departments(departments)


async def prefill_employees(employee_repository: EmployeeRepository) -> None:
    employees = []
    with open("/app/prefill/employees.json", "r") as file:
        employees_data = json.load(file)
        for emp in employees_data:
            employees.append(Employee(
                id=int(emp["id"]),
                department_id=int(emp["department_id"]),
                post_id=int(emp["post_id"]),
                first_name=emp["first_name"],
                last_name=emp["last_name"],
                phone_number=emp["phone_number"],
                city=emp["city"],
                birthdate=datetime.strptime(emp["birthdate"], "%Y.%m.%d") if emp.get("birthdate") else None,
                address=emp["address"],
                email="some_email@mts.ru",
                sex=emp["sex"],
                boss_id=int(emp["boss_id"]) if emp["boss_id"] else None
            ))

    await employee_repository.insert_prefill_employees(employees)


async def prefill_on_leaves(on_leave_repository: OnLeaveRepository) -> None:
    on_leaves = []
    with open("/app/prefill/on_leaves.json", "r") as file:
        on_leave_data = json.load(file)
        for on_leave in on_leave_data:
            on_leaves.append(OnLeave(
                id=on_leave["id"],
                employee_id=on_leave["employee_id"],
                date_from=datetime.strptime(on_leave["date_from"], "%Y.%m.%d")
                if on_leave.get("date_from") else None,
                date_to=datetime.strptime(on_leave["date_to"], "%Y.%m.%d")
                if on_leave.get("date_to") else None
            ))

    await on_leave_repository.insert_prefill_on_leaves(on_leaves)


async def prefill_on_sick_leaves(on_sick_leave_repository: OnSickLeaveRepository) -> None:
    on_sick_leaves = []
    with open("/app/prefill/on_sick_leaves.json", "r") as file:
        on_sick_leave_data = json.load(file)
        for on_sick_leave in on_sick_leave_data:
            on_sick_leaves.append(OnSickLeave(
                id=on_sick_leave["id"],
                employee_id=on_sick_leave["employee_id"],
                date_from=datetime.strptime(on_sick_leave["date_from"], "%Y.%m.%d")
                if on_sick_leave.get("date_from") else None,
                date_to=datetime.strptime(on_sick_leave["date_to"], "%Y.%m.%d")
                if on_sick_leave.get("date_to") else None
            ))

    await on_sick_leave_repository.insert_prefill_on_sick_leaves(on_sick_leaves)
