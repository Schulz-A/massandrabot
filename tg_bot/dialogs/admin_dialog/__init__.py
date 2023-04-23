from aiogram_dialog import Dialog

from tg_bot.dialogs.admin_dialog.users_dialog.windows import users_window, user_info_window
from tg_bot.dialogs.admin_dialog.windows import admin_functions_window


def admin_dialog():
    return Dialog(
        admin_functions_window(),
        users_window(),
        user_info_window()
    )
