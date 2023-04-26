import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import (Button, Group, Row, ScrollingGroup,
                                        Select)
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.admin_dialog.structure_dialog import (backs, getters,
                                                          keyboards, selected)
from tg_bot.misc.Enums import Enums


def structure_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Row(
            Button(Const("Проекты 🗃️"), id="projects_s", on_click=selected.on_projects),
            Button(Const("Категории 🗂️"), id="categories_s", on_click=selected.on_categories),
            Button(Const("Статьи 📋"), id="articles_s", on_click=selected.on_articles),
        ),
        Button(Const("⬅️ Назад"), id="back_to_adminp", on_click=backs.back_on_admin_panel),
        state=AdminPanelStates.structure_menu
    )


def projects_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Group(
            Select(
                Format("{item.name} ({item.abbreviation})"),
                id="project_stru_gr",
                item_id_getter=operator.attrgetter("id"),
                items="projects",
                on_click=selected.on_chosen_project
            ),
            width=2
        ),
        Button(Const("Добавить новый проект ➕"), id="start_adding", on_click=selected.start_adding_project),
        Button(Const("⬅️ Назад"), id="back_to_stru", on_click=backs.back_on_structure_panel),
        state=AdminPanelStates.projects_menu,
        getter=getters.get_projects_structure
    )


def categories_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        ScrollingGroup(
            Select(
                Format("{item.name} ({item.project.name})"),
                id="categories_stru_gr",
                item_id_getter=operator.attrgetter("id"),
                items="categories",
                on_click=selected.on_chosen_category
            ),
            id="scrolling_projects_structure",
            width=2, height=5,
            hide_on_single_page=True
        ),
        Button(Const("Добавить новую категорию ➕"), id="start_adding", on_click=selected.start_adding_category),
        Button(Const("⬅️ Назад"), id="back_to_stru", on_click=backs.back_on_structure_panel),
        state=AdminPanelStates.categories_menu,
        getter=getters.get_categories_structure
    )


def articles_window():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        ScrollingGroup(
            Select(
                Format("{item.name} ({item.project.name})"),
                id="articles_stru_gr",
                item_id_getter=operator.attrgetter("id"),
                items="articles",
                on_click=selected.on_chosen_article
            ),
            id="scrolling_articles_structure",
            width=2, height=5,
            hide_on_single_page=True
        ),
        Button(Const("Добавить новую статью ➕"), id="start_adding", on_click=selected.start_adding_article),
        Button(Const("⬅️ Назад"), id="back_to_stru", on_click=backs.back_on_structure_panel),
        state=AdminPanelStates.articles_menu,
        getter=getters.get_articles_structure
    )


def project_info():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Format("Проект: {name}"),
        keyboards.column_select(selected.on_chosen_column),
        Button(Const("Удалить проект 🗑️"), id="delete_button", on_click=selected.on_delete),
        Button(Const("⬅️ Назад"), id="back_to_pr", on_click=backs.back_on_items),
        state=AdminPanelStates.project_info,
        getter=getters.get_columns
    )


def category_info():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Format(
            "Категория: {name}\n"
            "Проекта: {project_name}"
        ),
        keyboards.column_select(selected.on_chosen_column),
        Button(Const("Удалить категорию 🗑️"), id="delete_button", on_click=selected.on_delete),
        Button(Const("⬅️ Назад"), id="back_to_cat", on_click=backs.back_on_items),
        state=AdminPanelStates.category_info,
        getter=getters.get_columns
    )


def article_info():
    return Window(
        StaticMedia(
            path=Enums.logo_path.value
        ),
        Format(
            "Статья: {name}\n"
            "Категории: {category_name}\n"
            "Проекта: {project_name}"
        ),
        keyboards.column_select(selected.on_chosen_column),
        Button(Const("Удалить статью 🗑️"), id="delete_button", on_click=selected.on_delete),
        Button(Const("⬅️ Назад"), id="back_to_pr", on_click=backs.back_on_items),
        state=AdminPanelStates.article_info,
        getter=getters.get_columns
    )


def change_column():
    return Window(
        Const("Напишите новое значение"),
        TextInput(
            id="entering",
            on_success=selected.on_entered,
            on_error=selected.on_entered
        ),
        Button(Const("Отменить ❌"), id="back_on_stru", on_click=backs.back_on_structure_panel),
        state=AdminPanelStates.change_column
    )


def except_delete_item():
    return Window(
        Const("Вы действительно хотите удалить элемент?"),
        Button(Const("Да ✅"), id="except_button", on_click=selected.on_except_delete),
        Button(Const("Отменить ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.except_delete_item
    )
