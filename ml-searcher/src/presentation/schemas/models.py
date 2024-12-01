from datetime import date
from typing import List, Dict, Any

from pydantic import BaseModel, EmailStr

from .on_leave_schema import OnLeaveSchema
from .on_sick_leave_schema import OnSickLeaveSchema



# Модель данных для запроса
class SearchRequest(BaseModel):
    data: Dict[str, Any]  # JSON данные сотрудников
    prompt: str  # Промпт для поиска

# Модель данных для ответа
class SearchResponse(BaseModel):
    matching_ids_name: Dict[int, str]


class Employee(BaseModel):
    id: int
    post: str | None = None
    department: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    birthdate: date | None = None
    sex: str | None = None
    phone_number: str | None = None
    city: str | None = None
    address: str | None = None
    tg_username: str | None = None
    email: EmailStr | None = None
    on_sick_leave_info: OnSickLeaveSchema | None = None
    on_leave_info: OnLeaveSchema | None = None
    boss_id: str | None = None
    about: str | None = None



class InputData(BaseModel):
    filtered_employees: List[Employee]
    prompt: str
    threshold: float = 0.7