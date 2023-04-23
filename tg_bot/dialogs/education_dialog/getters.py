from typing import List

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Group, Url
from aiogram_dialog.widgets.text import Const

from tg_bot.infrastucture.database.functions.queries import get_projects, get_categories, get_articles
from tg_bot.infrastucture.database.models import Category, Article


async def get_projects_to_window(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    projects = await get_projects(session)

    data = {
        "projects": projects
    }

    return data


async def get_category_to_window(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    project_id = dialog_manager.dialog_data.get("project_id")
    categories = await get_categories(session, Category.project_id == project_id)
    cat: Category = categories[0]
    print(cat.project.name)

    data = {
        "categories": categories
    }

    return data


async def get_articles_to_window(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    category_id = dialog_manager.dialog_data.get("category_id")
    articles: List[Article] = await get_articles(session, Article.category_id == category_id)

    data = {
        "articles": articles
    }

    return data
