from aiogram import types
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Select, Button

from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.dialogs.start_dialog.states import StartState


async def on_chosen_project(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, project_id: str):
    dialog_manager.dialog_data.update(project_id=project_id)
    await dialog_manager.switch_to(EducationStates.select_category)


async def on_chosen_category(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, category_id: str):
    dialog_manager.dialog_data.update(category_id=category_id)
    await dialog_manager.switch_to(EducationStates.select_article)


async def cancel_window(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await call.message.delete()
    await dialog_manager.start(StartState.start_state, mode=StartMode.NEW_STACK, show_mode=ShowMode.SEND)
