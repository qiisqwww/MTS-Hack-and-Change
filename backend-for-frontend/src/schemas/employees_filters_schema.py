from pydantic import BaseModel

__all__ = [
    "EmployeesFiltersSchema"
]


class EmployeesFiltersSchema(BaseModel):
    departments_id: list[str] | None
    post_id: str | None
    role_id: int | None
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    phone_number: str | None
    email: str | None
    tg_username: str | None
    city: str | None
    address: str | None
