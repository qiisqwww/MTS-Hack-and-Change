from src.config.env import StrEnv, IntEnv

__all__ = [
    "PROJECT_NAME",
    "DOCS_URL",
    "OPENAPI_URL",
    "HTTP_HOST",
    "HTTP_PORT"
]

PROJECT_NAME: str = StrEnv("PROJECT_NAME")

DOCS_URL: str = StrEnv("DOCS_URL")
OPENAPI_URL: str = StrEnv("OPENAPI_URL")

HTTP_HOST: str = StrEnv("HTTP_HOST")
HTTP_PORT: int = IntEnv("HTTP_PORT")
