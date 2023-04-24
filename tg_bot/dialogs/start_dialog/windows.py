from aiogram_dialog import Window, Data, DialogManager
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from tg_bot.dialogs.start_dialog import states, selected
from tg_bot.dialogs.start_dialog.states import StartState
from tg_bot.misc.Enums import Enums


def start_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Const("Добро пожаловать!!!"),
        Group(
            Button(Const("Обучение 📖"), id="education_button", on_click=selected.start_education_dialog),
            Button(Const("Тех. Состояние 🛠️"), id="fix_button", on_click=selected.start_fixer),
            Button(Const("Админ Панель 🎛️"), id="admin_panel_button", on_click=selected.start_admin_dialog),
            width=1
        ),
        state=states.StartState.start_state
    )
