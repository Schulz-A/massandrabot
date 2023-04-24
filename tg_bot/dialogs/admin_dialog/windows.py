from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Group
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from tg_bot.dialogs.admin_dialog import states
from tg_bot.dialogs.admin_dialog.structure_dialog.selected import open_structure_panel
from tg_bot.dialogs.admin_dialog.users_dialog.selected import open_users_panel
from tg_bot.dialogs.education_dialog.selected import cancel_window
from tg_bot.misc.Enums import Enums


def admin_functions_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Group(
            Button(Const("Пользователи"), id="users_panel", on_click=open_users_panel),
            Button(Const("Структура"), id="structure_panel", on_click=open_structure_panel),
            width=2
        ),
        Cancel(Const("Назад"), id="back_to_main", on_click=cancel_window),
        state=states.AdminPanelStates.select_admin_function
    )
