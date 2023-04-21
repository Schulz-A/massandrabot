from aiogram import Bot, Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.misc.startkeyboard import start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, bot: Bot):
    photo_url = "https://drive.google.com/uc?export=view&id=18TixwabEa6ICmVfgClK34JXa9jIQCRl0"
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption="HI!", reply_markup=start_keyboard)


@start_router.message()
async def start_education_dialog(message: types.Message):
    await message.answer("Hi")
