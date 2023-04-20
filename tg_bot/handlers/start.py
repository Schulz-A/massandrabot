from aiogram import Bot, Router, types
from aiogram.types import BufferedInputFile
from sqlalchemy.ext.asyncio import AsyncSession

from apis.imgbbapi import IMGBBClient
from tg_bot.config import Config
from tg_bot.misc.startkeyboard import start_keyboard

start_router = Router()


@start_router.message()
async def get_photo(message: types.Message, bot: Bot, image_client: IMGBBClient, config: Config, session: AsyncSession):
    print(session.__dict__)
    with open("logo.jpg", "rb") as photo:
        photo = BufferedInputFile(photo.read(), "logo")
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="HI!", reply_markup=start_keyboard)
