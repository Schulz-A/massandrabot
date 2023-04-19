from io import BytesIO

from aiogram import Bot, F, Router, types
from aiogram.types import InputFile, PhotoSize, BufferedInputFile

from massandrabot.config import Config
from massandrabot.infrastucture.apis.imgbbapi import IMGBBClient
from massandrabot.misc.startkeyboard import start_keyboard

start_router = Router()


@start_router.message()
async def get_photo(message: types.Message, bot: Bot, image_client: IMGBBClient, config: Config):
    with open("logo.jpg", "rb") as photo:
        photo = BufferedInputFile(photo.read(), "logo")
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="HI!", reply_markup=start_keyboard)
