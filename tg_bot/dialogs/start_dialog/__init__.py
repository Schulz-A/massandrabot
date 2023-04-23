from aiogram_dialog import Dialog

from tg_bot.dialogs.start_dialog.windows import start_window


def start_dialog():
    return Dialog(
        start_window(),
    )
