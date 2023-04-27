from aiogram_dialog import DialogManager

from tg_bot.infrastucture.database.functions.queries import (get_categories,
                                                             get_projects)
from tg_bot.infrastucture.database.models import Article, Category, Project


async def get_adding_project(dialog_manager: DialogManager, **middleware_data):
    table = dialog_manager.dialog_data.get("table")
    data = {}

    if table == Project.__tablename__:
        project_name = dialog_manager.dialog_data.get("project_name")
        project_abb = dialog_manager.dialog_data.get("project_abb")

        data = {
            "name": project_name,
            "abb": project_abb,
            "pro": True
        }

    if table == Category.__tablename__:
        project_name = dialog_manager.dialog_data.get("project_name")
        category_name = dialog_manager.dialog_data.get("category_name")

        data = {
            "name": category_name,
            "project_name": project_name,
            "cat": True
        }

    if table == Article.__tablename__:
        article_name = dialog_manager.dialog_data.get("article_name")
        category_name = dialog_manager.dialog_data.get("category_name")
        project_name = dialog_manager.dialog_data.get("project_name")

        data = {
            "name": article_name,
            "category_name": category_name,
            "project_name": project_name,
            "art": True
        }

    return data


async def get_pr_for_cat(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    projects = await get_projects(session)

    data = {
        "projects": projects
    }

    return data


async def get_cat_for_art(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    categories = await get_categories(session)

    data = {
        "categories": categories
    }

    return data
