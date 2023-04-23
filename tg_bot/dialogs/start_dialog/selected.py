from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.infrastucture.database.functions.queries import get_user
from tg_bot.infrastucture.database.models import User


async def start_education_dialog(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.start(EducationStates.select_project, mode=StartMode.RESET_STACK)


async def start_fixer(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state: FSMContext = dialog_manager.middleware_data.get("state")
    await state.set_state(state="start_fixing")


async def start_admin_dialog(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    session = dialog_manager.middleware_data.get("session")
    event_from_user = dialog_manager.middleware_data.get("event_from_user")
    user = await get_user(session, User.id == event_from_user.id)
    if not user.is_admin:
        await call.answer("Вы не являетесь администратором!!!", show_alert=True)
        return
    await dialog_manager.start(AdminPanelStates.select_admin_function, mode=StartMode.RESET_STACK)
