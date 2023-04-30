from aiogram.fsm.state import State, StatesGroup


class AdminPanelStates(StatesGroup):
    select_admin_function = State()
    select_user = State()
    user_info = State()
    except_delete_user = State()
    user_group = State()

    structure_menu = State()

    projects_menu = State()
    project_info = State()

    categories_menu = State()
    category_info = State()

    articles_menu = State()
    article_info = State()

    change_column = State()
    except_delete_item = State()

    project_name = State()
    project_abbreviation = State()
    project_except_add = State()

    category_name = State()
    category_project = State()
    category_except_add = State()

    article_name = State()
    article_url = State()
    article_category = State()
    article_except_add = State()

    redirects = {
        "projects": projects_menu,
        "categories": categories_menu,
        "articles": articles_menu
    }
