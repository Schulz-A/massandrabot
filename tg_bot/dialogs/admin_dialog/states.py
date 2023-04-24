from aiogram.fsm.state import StatesGroup, State


class AdminPanelStates(StatesGroup):
    select_admin_function = State()
    select_user = State()
    user_info = State()
    except_delete_user = State()

    structure_menu = State()

    projects_menu = State()
    project_info = State()

    categories_menu = State()
    category_info = State()

    articles_menu = State()
    article_info = State()

    change_column = State()
