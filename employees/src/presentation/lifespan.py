from fastapi import FastAPI

from contextlib import asynccontextmanager
import asyncio

from src.prefill_database import prefill_database


__all__ = [
    "lifespan"
]


@asynccontextmanager
async def lifespan(_: FastAPI):
    process = await asyncio.create_subprocess_exec(
        'alembic', 'upgrade', 'head',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    _, _ = await process.communicate()

    await prefill_database()

    yield
