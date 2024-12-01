from datetime import date

from pydantic import BaseModel

__all__ = [
    "OnSickLeaveSchema",
]


class OnSickLeaveSchema(BaseModel):
    date_from: date
    date_to: date
