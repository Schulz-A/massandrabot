from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates


async def back_on_admin_panel(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.select_admin_function)


async def back_on_structure_panel(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.structure_menu)


async def back_on_projects(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.projects_menu)


async def back_on_categories(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.categories_menu)


async def back_on_articles(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.articles_menu)
