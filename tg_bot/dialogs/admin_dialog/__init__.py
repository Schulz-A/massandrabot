from aiogram_dialog import Dialog

from tg_bot.dialogs.admin_dialog.structure_dialog.windows import structure_window, projects_window, categories_window, \
    articles_window, project_info, category_info, article_info
from tg_bot.dialogs.admin_dialog.users_dialog.windows import users_window, user_info_window, except_delete_window
from tg_bot.dialogs.admin_dialog.windows import admin_functions_window


def admin_dialog():
    return Dialog(
        admin_functions_window(),
        users_window(),
        user_info_window(),
        except_delete_window(),

        structure_window(),
        projects_window(),
        categories_window(),
        articles_window(),

        project_info(),
        category_info(),
        article_info()

    )
