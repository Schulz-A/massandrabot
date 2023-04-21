import asyncio
import os

from aiogram import Bot, Router, types, F
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.infrastucture.database.functions.queries import get_user
from tg_bot.infrastucture.database.models import User
from tg_bot.misc.startkeyboard import start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, bot: Bot):
    photo_url = "https://drive.google.com/uc?export=view&id=18TixwabEa6ICmVfgClK34JXa9jIQCRl0"
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption="HI!", reply_markup=start_keyboard)


@start_router.message()
async def start_education_dialog(message: types.Message):
    await message.answer("Hi")


# @start_router.message(F.text == "удалить")
# async def delete_photo(message: types.Message, session: AsyncSession):
#     user = await get_user(session, User.id == message.from_user.id)
#
#     await asyncio.to_thread(os.unlink, user.photo_path)
