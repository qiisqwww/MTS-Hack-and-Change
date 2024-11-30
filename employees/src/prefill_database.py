import json

from src.repositories.impls import (
    RoleRepository,
    PostRepository,
    DepartmentRepository,
    EmployeeRepository
)
from src.entities.models import Role, Post, Employee, Department
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
                address=emp["address"],
                email="some_email@mts.ru",
                boss_id=int(emp["boss_id"]) if emp["boss_id"] else None
            ))

    await employee_repository.insert_prefill_employees(employees)
