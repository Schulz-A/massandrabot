from aiogram_dialog import Dialog

from tg_bot.dialogs.education_dialog.windows import (chose_article_window,
                                                     chose_category_window,
                                                     chose_project_window)


def education_dialog():
    return Dialog(
        chose_project_window(),
        chose_category_window(),
        chose_article_window()

    )
