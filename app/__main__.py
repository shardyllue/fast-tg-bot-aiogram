from aiogram import executor
from loguru import logger

from core import Dispatcher, dp
from core.middleware import ThrottlingMiddleware

from db import Session

from handler import dp

async def on_startup(dp : Dispatcher):
    logger.info("Start up")
    dp.middleware.setup(ThrottlingMiddleware(Session))


async def on_shutdown(dp : Dispatcher):
    logger.info("Shutdown down")


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )