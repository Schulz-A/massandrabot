from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.infrastucture.database.functions.queries import update_user, delete_user
from tg_bot.infrastucture.database.models import User


async def open_users_panel(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.select_user)


async def on_chosen_user(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, user_id: str):
    dialog_manager.dialog_data.update(user_id=int(user_id))
    await dialog_manager.switch_to(AdminPanelStates.user_info)


async def on_allow(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    session = dialog_manager.middleware_data.get("session")
    allow = dialog_manager.dialog_data.get("allow")
    user_id = dialog_manager.dialog_data.get("user_id")

    await update_user(session, User.id == user_id, allow=not allow)


async def on_admin(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    session = dialog_manager.middleware_data.get("session")
    is_admin = dialog_manager.dialog_data.get("is_admin")
    user_id = dialog_manager.dialog_data.get("user_id")

    await update_user(session, User.id == user_id, is_admin=not is_admin)


async def on_delete_user(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.except_delete_user)


async def except_deleting(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    session = dialog_manager.middleware_data.get("session")
    user_id = dialog_manager.dialog_data.get("user_id")

    full_name = await delete_user(session, User.id == user_id)

    await call.answer(f"Пользователь {full_name} удален!", show_alert=True)

    await dialog_manager.switch_to(AdminPanelStates.select_user)
