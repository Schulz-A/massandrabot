from aiogram_dialog import DialogManager

from tg_bot.infrastucture.database.functions.queries import get_projects, get_categories, get_articles
from tg_bot.infrastucture.database.models import Project, Category, Article


async def get_projects_structure(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")

    project = await get_projects(session)

    data = {
        "projects": project
    }

    return data


async def get_categories_structure(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")

    categories = await get_categories(session)

    data = {
        "categories": categories
    }

    return data


async def get_articles_structure(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")

    articles = await get_articles(session)

    data = {
        "articles": articles
    }

    return data


async def get_columns(dialog_manager: DialogManager, **middleware_data):
    table = dialog_manager.dialog_data.get("table")
    session = middleware_data.get("session")
    data = {}

    if table == Project:
        project_id = dialog_manager.dialog_data.get("project_id")
        project = await get_projects(session, Project.id == project_id)
        coll_names = [("Название проекта", "name")]
        data = {"coll_names": coll_names, "name": project[0].name}

    if table == Category:
        category_id = dialog_manager.dialog_data.get("category_id")
        category = await get_categories(session, Category.id == category_id)
        coll_names = [("Название проекта", "name")]
        data = {"coll_names": coll_names, "name": category[0].name, "project_name": category[0].project.name}

    if table == Article:
        article_id = dialog_manager.dialog_data.get("article_id")
        article = await get_articles(session, Article.id == article_id)
        coll_names = [("Название проекта", "name"), ("ссылка", "url")]
        data = {
            "coll_names": coll_names,
            "name": article[0].name,
            "category_name": article[0].category.name,
            "project_name": article[0].category.project.name
        }

    return data
