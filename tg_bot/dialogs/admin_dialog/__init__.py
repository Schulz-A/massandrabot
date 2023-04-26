from aiogram_dialog import Dialog

from tg_bot.dialogs.admin_dialog.structure_dialog.addingselect import enter_project_name
from tg_bot.dialogs.admin_dialog.structure_dialog.addingwindows import enter_project_name, enter_project_abbreviation, \
    except_adding, enter_category_name, enter_project_for_category, enter_article_name, enter_article_url, \
    enter_category_for_article
from tg_bot.dialogs.admin_dialog.structure_dialog.windows import (
    article_info, articles_window, categories_window, category_info,
    change_column, project_info, projects_window, structure_window, except_delete_item)
from tg_bot.dialogs.admin_dialog.users_dialog.windows import (
    except_delete_window, user_info_window, users_window)
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
        article_info(),

        except_delete_item(),

        change_column(),

        enter_project_name(),
        enter_project_abbreviation(),
        except_adding(),

        enter_category_name(),
        enter_project_for_category(),

        enter_article_name(),
        enter_article_url(),
        enter_category_for_article()

    )
