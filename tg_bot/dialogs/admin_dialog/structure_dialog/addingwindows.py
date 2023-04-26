import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from tg_bot.dialogs.admin_dialog.states import AdminPanelStates
from tg_bot.dialogs.admin_dialog.structure_dialog import addingselect, backs, addinggetters


def enter_project_name():
    return Window(
        Const("Введите название для проекта"),
        TextInput(
            id="name_for_project",
            on_success=addingselect.enter_project_name
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.project_name
    )


def enter_project_abbreviation():
    return Window(
        Const("Введите аббревиатуру для проекта"),
        TextInput(
            id="abbrv_for_project",
            on_success=addingselect.enter_project_abbreviation
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.project_abbreviation
    )


def except_adding():
    return Window(
        Format(
            "Проект, который вы хотите добавить\n\n"
            "Имя: {name}\n"
            "Аббревиатура: {abb}",
            when="pro"
        ),
        Format(
            "Категория, которую вы хотите добавить\n\n"
            "Имя: {name}\n"
            "Проекта: {project_name}",
            when="cat"
        ),
        Format(
            "Статья, которую вы хотите добавить\n\n"
            "Имя: {name}\n"
            "Категории: {category_name}\n"
            "Проекта: {project_name}",
            when="art"
        ),
        Button(Const("Да ✅"), id="except_add", on_click=addingselect.except_add),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.project_except_add,
        getter=addinggetters.get_adding_project
    )


def enter_category_name():
    return Window(
        Const("Введите название для категории"),
        TextInput(
            id="name_for_category",
            on_success=addingselect.enter_category_name
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.category_name
    )


def enter_project_for_category():
    return Window(
        Const("Выберите проект для категории"),
        ScrollingGroup(
            Select(
                Format("{item.name}"),
                id="projects_group",
                item_id_getter=operator.attrgetter("id"),
                items="projects",
                on_click=addingselect.chose_pr_for_cat
            ),
            id="projects_scrolling",
            width=2, height=4
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.category_project,
        getter=addinggetters.get_pr_for_cat
    )


def enter_article_name():
    return Window(
        Const("Введите название для статьи"),
        TextInput(
            id="name_for_article",
            on_success=addingselect.enter_article_name
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.article_name
    )


def enter_article_url():
    return Window(
        Const("Введите url адрес для статьи"),
        TextInput(
            id="url_for_article",
            on_success=addingselect.enter_article_url
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.article_url
    )


def enter_category_for_article():
    return Window(
        Const("Выберите категорию для статьи"),
        ScrollingGroup(
            Select(
                Format("{item.name} ({item.project.abbreviation})"),
                id="categories_group",
                item_id_getter=operator.attrgetter("id"),
                items="categories",
                on_click=addingselect.chose_cat_for_art
            ),
            id="categories_scrolling",
            width=2, height=4
        ),
        Button(Const("Отмена ❌"), id="back_to_items", on_click=backs.back_on_items),
        state=AdminPanelStates.article_category,
        getter=addinggetters.get_cat_for_art
    )
