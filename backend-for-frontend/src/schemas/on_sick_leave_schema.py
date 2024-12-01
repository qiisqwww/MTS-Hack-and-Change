from datetime import date

from pydantic import BaseModel

__all__ = [
    "OnSickLeaveSchema",
]


class OnSickLeaveSchema(BaseModel):
    date_from: str
    date_to: str
