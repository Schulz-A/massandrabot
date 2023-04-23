from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Group
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from tg_bot.dialogs.admin_dialog import states
from tg_bot.dialogs.admin_dialog.users_dialog.selected import open_users_panel
from tg_bot.dialogs.education_dialog.selected import cancel_window


def admin_functions_window():
    return Window(
        StaticMedia(
            path="logo.jpg"
        ),
        Group(
            Button(Const("Пользователи"), id="users_panel", on_click=open_users_panel),
            Button(Const("Структура"), id="structure_panel", ),
            width=2
        ),
        Cancel(Const("Назад"), id="back_to_main", on_click=cancel_window),
        state=states.AdminPanelStates.select_admin_function
    )
