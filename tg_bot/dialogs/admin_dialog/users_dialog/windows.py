import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (Back, Button, Group, ScrollingGroup,
                                        Select)
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.admin_dialog.users_dialog import getters, selected
from tg_bot.misc.Enums import Enums


def users_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
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
        Back(Const("⬅️ Назад")),
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
            "Является администратором: {is_admin}\n"
            "Группа: {group}"
        ),
        Group(
            Button(Const("Разрешить/Запретить доступ"), id="change_allow", on_click=selected.on_allow),
            Button(Const("Разрешить/Запретить администрирование"), id="change_admin", on_click=selected.on_admin),
            Button(Const("Выбрать группу"), id="chose_group", on_click=selected.on_groups),
            width=1
        ),
        Button(Const("Удалить пользователя 🗑️"), id="delete_user", on_click=selected.on_delete_user),
        Back(Const("⬅️ Назад")),
        state=AdminPanelStates.user_info,
        getter=getters.get_user_info
    )


def user_group_window():
    return Window(
        Format("Выбери группу для пользователя"),
        Group(
            Select(
                Format("{item.name}"),
                id="projects_group",
                item_id_getter=operator.attrgetter("id"),
                items="projects",
                on_click=selected.on_chosen_group
            ),
            width=2
        ),
        Button(Const("Суперюзер 🥷"), id="superuser", on_click=selected.on_superuser),
        Button(Const("Очистить группы ♻️"), id="clear_group", on_click=selected.on_clear_group),
        Button(Const("⬅️ Назад"), id="back_to_user", on_click=selected.back_to_user),
        state=AdminPanelStates.user_group,
        getter=getters.get_projects_to_window
    )


def except_delete_window():
    return Window(
        Format("Вы действительно хотите удалить пользователя: {full_name}"),
        Button(Const("Да ✅"), id="except_deleting_button", on_click=selected.except_deleting),
        Back(Const("⬅️ Назад")),
        state=AdminPanelStates.except_delete_user,
        getter=getters.get_deleting_user
    )
