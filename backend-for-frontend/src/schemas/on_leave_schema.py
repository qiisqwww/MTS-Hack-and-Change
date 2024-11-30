from datetime import date

from pydantic import BaseModel

__all__ = [
    "OnLeaveSchema",
]


class OnLeaveSchema(BaseModel):
    employee_id: int
    date_from: date
    date_to: date
