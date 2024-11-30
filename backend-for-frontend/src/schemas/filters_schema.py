from pydantic import BaseModel

__all__ = [
    "FiltersSchema",
]


class FiltersSchema(BaseModel):
    departments: list[str] | None
    post: str | None
    role: str | None
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    phone_number: str | None
    city: str | None
    address: str | None
    email: str | None
    prompt: str | None
