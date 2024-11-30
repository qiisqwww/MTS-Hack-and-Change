from typing import List

from pydantic import BaseModel



class Employee(BaseModel):
    id: int
    post: str
    department: str
    first_name: str
    last_name: str
    birthdate: str
    sex: str
    phone_number: str
    city: str
    address: str
    tg_username: str
    email: str
    on_sick_leave_info: str
    on_leave_info: str
    boss_id: str
    about: str


class InputData(BaseModel):
    filtered_employees: List[Employee]
    prompt: str
    threshold: float = 0.7