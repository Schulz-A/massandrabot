from aiogram_dialog import DialogRegistry

from tg_bot.dialogs.admin_dialog import admin_dialog
from tg_bot.dialogs.education_dialog import education_dialog
from tg_bot.dialogs.start_dialog import start_dialog


def register_all_dialogs(dp):
    registry = DialogRegistry(dp=dp)

    for dialog in [
        start_dialog(),
        education_dialog(),
        admin_dialog()
    ]:
        registry.register(dialog)
