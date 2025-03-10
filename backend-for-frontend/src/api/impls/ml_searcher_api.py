from aiohttp import ClientSession
from fastapi.encoders import jsonable_encoder

from src.api.interfaces import IMLSearcherApi
from src.schemas.employee_temp_schema import EmployeeTempSchema

__all__ = [
    "MLSearcherApi",
]


class MLSearcherApi(IMLSearcherApi):
    _ML_SEARCHER_URL = "http://ml-searcher:8081"

    async def filter_by_prompt(self, prompt: str, employees: list[EmployeeTempSchema]) -> list[int]:
        async with ClientSession() as session:
            try:
                response = await session.post(
                    self._ML_SEARCHER_URL + "/api/filter",
                    json={
                        "data": {
                            "filtered_employees": [jsonable_encoder(emp) for emp in employees]
                        },
                        "prompt": prompt
                    }
                )
            except Exception as e:
                print(e)
                return []

            if response.status != 200:
                return []

            matching_ids = await response.json(encoding="utf-8")

        return list(map(int, matching_ids.get("matching_ids", {})))
