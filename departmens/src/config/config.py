from src.config.env import StrEnv, IntEnv

__all__ = [
    "PROJECT_NAME",
    "DOCS_URL",
    "OPENAPI_URL",
    "HTTP_HOST",
    "HTTP_PORT",
    "DB_HOST",
    "DB_NAME",
    "DB_PORT",
    "DB_PASS",
    "DB_USER"
]

PROJECT_NAME: str = StrEnv("PROJECT_NAME")

DOCS_URL: str = StrEnv("DOCS_URL")
OPENAPI_URL: str = StrEnv("OPENAPI_URL")

HTTP_HOST: str = StrEnv("HTTP_HOST")
HTTP_PORT: int = IntEnv("HTTP_PORT")

DB_USER: str = StrEnv("DB_USER")
DB_PASS: str = StrEnv("DB_PASS")
DB_NAME: str = StrEnv("DB_NAME")
DB_HOST: str = StrEnv("DB_HOST")
DB_PORT: int = IntEnv("DB_PORT")
