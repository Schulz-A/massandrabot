from aiogram import Bot, F, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile
from aiogram_dialog import DialogManager, StartMode

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.misc.Enums import Enums
from tg_bot.misc.startkeyboard import start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, dialog_manager: DialogManager, bot: Bot, state: FSMContext):
    photo = BufferedInputFile.from_file(Enums.logo_path.value, "logo")
    del_m = await bot.send_photo(message.chat.id, photo=photo, caption="hi", reply_markup=start_keyboard)
    await state.update_data(mess_id=del_m.message_id)


@start_router.callback_query(F.data == "education")
async def start_education_dialog(call: types.CallbackQuery, dialog_manager: DialogManager, bot: Bot, state: FSMContext):
    data = await state.get_data()
    mess_id = data.get("mess_id")
    await bot.delete_message(call.message.chat.id, mess_id)
    await dialog_manager.start(EducationStates.select_project, mode=StartMode.RESET_STACK)


@start_router.callback_query(F.data == "admin_panel")
async def start_admin_panel(call: types.CallbackQuery, dialog_manager: DialogManager, bot: Bot, state: FSMContext):
    data = await state.get_data()
    mess_id = data.get("mess_id")
    await bot.delete_message(call.message.chat.id, mess_id)
    await dialog_manager.start(AdminPanelStates.select_admin_function, mode=StartMode.RESET_STACK)


# @start_router.message(F.text == "удалить")
# async def delete_photo(message: types.Message, session: AsyncSession):
#     user = await get_user(session, User.id == message.from_user.id)
#
#     await asyncio.to_thread(os.unlink, user.photo_path)
