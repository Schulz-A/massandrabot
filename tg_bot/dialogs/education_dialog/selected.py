from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.handlers.start import start_bot


async def on_chosen_project(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, project_id: str):
    dialog_manager.dialog_data.update(project_id=project_id)
    await dialog_manager.switch_to(EducationStates.select_category)


async def on_chosen_category(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, cat_id: str):
    dialog_manager.dialog_data.update(category_id=cat_id)
    await dialog_manager.switch_to(EducationStates.select_article)


async def cancel_window(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    bot = dialog_manager.middleware_data.get("bot")
    state = dialog_manager.middleware_data.get("state")
    await call.message.delete()
    await start_bot(call.message, dialog_manager, bot, state)
