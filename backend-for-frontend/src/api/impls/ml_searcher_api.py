from src.api.interfaces import IMLSearcherApi

__all__ = [
    "MLSearcherApi",
]


class MLSearcherApi(IMLSearcherApi):
    _ML_SEARCHER_URL = "http://ml-searcher:8081"

    async def filter_by_prompt(self, prompt: str, employees: list) -> list[int]:
        pass
