import asyncio

import uvicorn

from src.presentation import app_object
from src.config import HTTP_HOST, HTTP_PORT
from src.prefill_database import prefill_database


async def main() -> None:
    server_config = uvicorn.Config(app_object, host=HTTP_HOST, port=HTTP_PORT)
    server = uvicorn.Server(server_config)

    await prefill_database()

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
