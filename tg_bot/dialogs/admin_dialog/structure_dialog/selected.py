import asyncio

from aiogram import Bot, types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.infrastucture.database.functions.queries import update_item, delete_item
from tg_bot.infrastucture.database.models import Article, Category, Project
from tg_bot.misc.Enums import tables
from tg_bot.misc.validators import validators


async def open_structure_panel(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.structure_menu)


async def on_projects(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Project.__tablename__)
    await dialog_manager.switch_to(AdminPanelStates.projects_menu)


async def on_categories(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Category.__tablename__)
    await dialog_manager.switch_to(AdminPanelStates.categories_menu)


async def on_articles(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(table=Article.__tablename__)
    await dialog_manager.switch_to(AdminPanelStates.articles_menu)


async def on_chosen_project(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, project_id: str):
    dialog_manager.dialog_data.update(project_id=project_id, main_id=project_id)
    await dialog_manager.switch_to(AdminPanelStates.project_info)


async def on_chosen_category(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, cat_id: str):
    dialog_manager.dialog_data.update(category_id=cat_id, main_id=cat_id)
    await dialog_manager.switch_to(AdminPanelStates.category_info)


async def on_chosen_article(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, article_id: str):
    dialog_manager.dialog_data.update(article_id=article_id, main_id=article_id)
    await dialog_manager.switch_to(AdminPanelStates.article_info)


async def on_chosen_column(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, column_name: str):
    dialog_manager.dialog_data.update(column_name=column_name)
    await dialog_manager.switch_to(AdminPanelStates.change_column)


async def on_entered(message: types.Message, widget: TextInput, dialog_manager: DialogManager, userprint: str):
    bot: Bot = dialog_manager.middleware_data.get("bot")
    session = dialog_manager.middleware_data.get("session")
    column_name = dialog_manager.dialog_data.get("column_name")
    table = dialog_manager.dialog_data.get("table")
    main_id = dialog_manager.dialog_data.get("main_id")

    try:
        result = validators[column_name](userprint)
    except ValueError as e:
        text = e.args[0]
        del_message = await message.answer(text=text)
        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.chat.id, message_id=del_message.message_id-2)
        await message.delete()

        return

    await update_item(session, tables[table], tables[table].id == main_id, **{column_name: result})
    await message.delete()

    await message.answer("Значение измененно")
    await asyncio.sleep(1)
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id-1
    )

    await dialog_manager.switch_to(AdminPanelStates.redirects[table])


async def on_delete(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.except_delete_item)


async def on_except_delete(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    table = dialog_manager.dialog_data.get("table")
    main_id = dialog_manager.dialog_data.get("main_id")
    session = dialog_manager.middleware_data.get("session")

    await delete_item(session, tables[table], tables[table].id == main_id)

    await call.answer("Объект удален", show_alert=True)

    await dialog_manager.switch_to(AdminPanelStates.redirects[table])


async def start_adding_project(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.project_name)


async def start_adding_category(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.category_name)


async def start_adding_article(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(AdminPanelStates.article_name)
