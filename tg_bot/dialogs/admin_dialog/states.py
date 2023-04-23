from aiogram.fsm.state import StatesGroup, State


class AdminPanelStates(StatesGroup):
    select_admin_function = State()
    select_user = State()
    user_info = State()
    structure_menu = State()
    projects_menu = State()
    project_info = State()
    change_project = State()
    categories_menu = State()
    category_info = State()
    change_category = State()
    articles_menu = State()
    article_info = State()
    change_article = State()
