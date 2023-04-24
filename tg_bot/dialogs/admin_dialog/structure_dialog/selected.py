import asyncio

from aiogram import types, Bot
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.infrastucture.database.models import Article, Category, Project
from tg_bot.misc.validators import validators


async def open_structure_panel(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.structure_menu)


async def on_projects(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Project)
    await dialog_manager.switch_to(AdminPanelStates.projects_menu)


async def on_categories(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Category)
    await dialog_manager.switch_to(AdminPanelStates.categories_menu)


async def on_articles(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Article)
    await dialog_manager.switch_to(AdminPanelStates.articles_menu)


async def on_chosen_project(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, project_id: str):
    dialog_manager.dialog_data.update(project_id=project_id)
    await dialog_manager.switch_to(AdminPanelStates.project_info)


async def on_chosen_category(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, cat_id: str):
    dialog_manager.dialog_data.update(category_id=cat_id)
    await dialog_manager.switch_to(AdminPanelStates.category_info)


async def on_chosen_article(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, article_id: str):
    dialog_manager.dialog_data.update(article_id=article_id)
    await dialog_manager.switch_to(AdminPanelStates.article_info)


async def on_chosen_column(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, column_name: str):
    dialog_manager.dialog_data.update(column_name=column_name)
    await dialog_manager.switch_to(AdminPanelStates.change_column)


async def on_entered(message: types.Message, widget: TextInput, dialog_manager: DialogManager, userprint: str):
    bot: Bot = dialog_manager.middleware_data.get("bot")
    session = dialog_manager.middleware_data.get("session")
    column_name = dialog_manager.dialog_data.get("column_name")
    item_name = dialog_manager.dialog_data.get("item_name")

    try:
        result = validators[column_name](userprint)
    except ValueError as e:
        text = e.args[0]
        del_message = await message.answer(text=text)
        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.chat.id, message_id=del_message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=del_message.message_id-2)
        await message.delete()

        return

