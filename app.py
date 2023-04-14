import asyncio

import betterlogging
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from massandrabot.config import get_config
from massandrabot.infrastucture.database.setupdb import create_session_pool

betterlogging.basic_colorized_config(level="INFO")


def register_all_middlewares(dp: Dispatcher, session_pool):
    pass


async def main():
    config = get_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage, config=config)
    session_pool = await create_session_pool(config.db_config)

    routers = [

    ]

    dp.include_routers(*routers)

    register_all_middlewares(dp, session_pool)

    await dp.start_polling(bot)


if __name__ == "main":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemError):
        betterlogging.error("Bot stopped!!!")
