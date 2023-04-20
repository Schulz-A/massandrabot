import asyncio

import betterlogging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from apis.imgbbapi import IMGBBClient
from tg_bot.config import get_config
from tg_bot.handlers.fixer_handlers import fix_router
from tg_bot.handlers.start import start_router
from tg_bot.infrastucture.database.functions.setup import create_session_pool
from tg_bot.middlewares.dbmiddleware import DataBaseMiddleWare

betterlogging.basic_colorized_config(level="INFO")


async def on_shutdown(dp: Dispatcher):
    image_client: IMGBBClient = dp["image_client"]
    await image_client.close()


def register_all_middlewares(dp: Dispatcher, session_pool):
    dp.message.outer_middleware(DataBaseMiddleWare(session_pool))
    dp.callback_query.outer_middleware(DataBaseMiddleWare(session_pool))
    dp.callback_query.middleware(CallbackAnswerMiddleware())


async def main():
    config = get_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    storage = MemoryStorage()
    image_client = IMGBBClient(config.miscellaneous.photo_host)

    dp = Dispatcher(storage=storage, config=config, image_client=image_client)
    session_pool = await create_session_pool(config.db_config)
    print(session_pool)

    routers = [
        start_router,
        fix_router

    ]

    dp.include_routers(*routers)

    register_all_middlewares(dp, session_pool)


    await dp.start_polling(bot)
    # finally:
    #     await on_shutdown(dp)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemError):
        betterlogging.error("Bot stopped!!!")
