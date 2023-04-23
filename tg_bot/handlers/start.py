import asyncio
import os

from aiogram import Bot, Router, types, F
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, ShowMode, StartMode

from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.dialogs.start_dialog.states import StartState

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.SEND
    await dialog_manager.start(StartState.start_state, mode=StartMode.RESET_STACK)


# @start_router.callback_query(F.data == "education")
# async def start_education_dialog(call: types.CallbackQuery, dialog_manager: DialogManager):
#     # dialog_manager.show_mode = ShowMode.SEND
#     await dialog_manager.start(EducationStates.select_project, mode=StartMode.RESET_STACK)


# @start_router.message(F.text == "удалить")
# async def delete_photo(message: types.Message, session: AsyncSession):
#     user = await get_user(session, User.id == message.from_user.id)
#
#     await asyncio.to_thread(os.unlink, user.photo_path)
