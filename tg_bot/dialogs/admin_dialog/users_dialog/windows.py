import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Back, Group, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.admin_dialog.users_dialog import selected, getters


def users_window():
    return Window(
        StaticMedia(
            path="logo.jpg"
        ),
        ScrollingGroup(
            Select(
                Format("{item.full_name}"),
                id="users_group",
                item_id_getter=operator.attrgetter("id"),
                items="users",
                on_click=selected.on_chosen_user
            ),
            id="scrolling_users",
            width=2, height=5
        ),
        Back(Const("Назад")),
        state=AdminPanelStates.select_user,
        getter=getters.get_users_to_window
    )


def user_info_window():
    return Window(
        StaticMedia(
            path=Format("{path}")
        ),
        Format(
            "Пользователь: {full_name}\n"
            "ID: {id}\n"
            "Доступ: {allow}\n"
            "Является администратором: {is_admin}"
        ),
        Group(
            Button(Const("Разрешить/Запретить доступ"), id="change_allow", on_click=selected.on_allow),
            Button(Const("Разрешить/Запретить администрирование"), id="change_admin", on_click=selected.on_admin),
            width=2
        ),
        # Button(Const("Удалить пользователя"), id="delete_user", on_click=selected.on_delete_user),
        Back(Const("Назад")),
        state=AdminPanelStates.user_info,
        getter=getters.get_user_info
    )
