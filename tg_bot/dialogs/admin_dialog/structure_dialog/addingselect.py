from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.infrastucture.database.functions.queries import (add_item,
                                                             get_categories,
                                                             get_projects)
from tg_bot.infrastucture.database.models import Article, Category, Project
from tg_bot.misc.Enums import tables
from tg_bot.misc.validators import validators


async def enter_project_name(message: types.Message, widget: TextInput, dialog_manager: DialogManager, name: str):
    try:
        validators["name"](name)
    except ValueError as e:
        text = e.args[0]
        await message.answer(text=text)

        return

    dialog_manager.dialog_data.update(project_name=name)
    await dialog_manager.switch_to(AdminPanelStates.project_abbreviation)
    # await call.message.delete()


async def enter_project_abbreviation(message: types.Message, widge: TextInput, dialog_manager: DialogManager, abb: str):
    try:
        validators["abbreviation"](abb)
    except ValueError as e:
        text = e.args[0]
        await message.answer(text=text)

        return

    dialog_manager.dialog_data.update(project_abb=abb)
    await dialog_manager.switch_to(AdminPanelStates.project_except_add)


async def except_add(call: types.CallbackQuery, widget: Button, dialog_manager: DialogManager):
    table = dialog_manager.dialog_data.get("table")
    session = dialog_manager.middleware_data.get("session")
    values = {}

    if table == Project.__tablename__:
        project_name = dialog_manager.dialog_data.get("project_name")
        project_abb = dialog_manager.dialog_data.get("project_abb")

        values = {
            "name": project_name,
            "abbreviation": project_abb
        }

    if table == Category.__tablename__:
        project_id = dialog_manager.dialog_data.get("project_id")
        category_name = dialog_manager.dialog_data.get("category_name")

        values = {
            "name": category_name,
            "project_id": project_id
        }

    if table == Article.__tablename__:
        article_name = dialog_manager.dialog_data.get("article_name")
        url = dialog_manager.dialog_data.get("article_url")
        category_id = dialog_manager.dialog_data.get("category_id")
        project_id = dialog_manager.dialog_data.get("project_id")

        values = {
            "name": article_name,
            "url": url,
            "category_id": category_id,
            "project_id": project_id
        }

    await add_item(session, tables[table], **values)

    await dialog_manager.switch_to(AdminPanelStates.redirects[table])


async def enter_category_name(message: types.Message, widget: TextInput, dialog_manager: DialogManager, cat_name: str):
    try:
        validators["name"](cat_name)
    except ValueError as e:
        text = e.args[0]
        await message.answer(text=text)

        return

    dialog_manager.dialog_data.update(category_name=cat_name)
    await dialog_manager.switch_to(AdminPanelStates.category_project)


async def chose_pr_for_cat(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, project_id: str):
    session = dialog_manager.middleware_data.get("session")
    project = await get_projects(session, Project.id == project_id)
    dialog_manager.dialog_data.update(project_name=project[0].name)
    dialog_manager.dialog_data.update(project_id=project_id)
    await dialog_manager.switch_to(AdminPanelStates.project_except_add)


async def enter_article_name(message: types.Message, widget: TextInput, dialog_manager: DialogManager, art_name: str):
    try:
        validators["name"](art_name)
    except ValueError as e:
        text = e.args[0]
        await message.answer(text=text)

        return

    dialog_manager.dialog_data.update(article_name=art_name)
    await dialog_manager.switch_to(AdminPanelStates.article_url)


async def enter_article_url(message: types.Message, widget: TextInput, dialog_manager: DialogManager, art_url: str):
    try:
        validators["url"](art_url)
    except ValueError as e:
        text = e.args[0]
        await message.answer(text=text)

        return

    dialog_manager.dialog_data.update(article_url=art_url)
    await dialog_manager.switch_to(AdminPanelStates.article_category)


async def chose_cat_for_art(call: types.CallbackQuery, widget: Select, dialog_manager: DialogManager, cat_id: str):
    session = dialog_manager.middleware_data.get("session")
    category = await get_categories(session, Category.id == cat_id)
    dialog_manager.dialog_data.update(category_name=category[0].name)
    dialog_manager.dialog_data.update(project_name=category[0].project.name)
    dialog_manager.dialog_data.update(project_id=str(category[0].project.id))
    dialog_manager.dialog_data.update(category_id=cat_id)
    await dialog_manager.switch_to(AdminPanelStates.project_except_add)
