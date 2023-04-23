import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Back, Group, Select, Url
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from tg_bot.dialogs.education_dialog import keyboards, selected, getters
from tg_bot.dialogs.education_dialog.states import EducationStates
from tg_bot.misc.SelectURL import SelectURL


def chose_project_window():
    return Window(
        StaticMedia(
            path="logo.jpg"
        ),
        Format("Выбери проект!"),
        keyboards.paginated_projects(selected.on_chosen_project),
        Cancel(Const("Назад"), id="back_to_strt", on_click=selected.cancel_window),
        state=EducationStates.select_project,
        getter=getters.get_projects_to_window
    )


def chose_category_window():
    return Window(
        StaticMedia(
            path="logo.jpg"
        ),
        Const("Выбери категорию!"),
        Group(
            Select(
                Format("{item.name}"),
                id="category_group",
                item_id_getter=operator.attrgetter("id"),
                items="categories",
                on_click=selected.on_chosen_category
            ),
            width=2
        ),
        Back(Const("Back")),
        state=EducationStates.select_category,
        getter=getters.get_category_to_window
    )


def chose_article_window():
    return Window(
        StaticMedia(
            path="logo.jpg"
        ),
        Const("hi"),
        Group(
            SelectURL(
                text=Format("{item.name}"),
                url=Format("{item.url}"),
                id="articles_group",
                item_id_getter=operator.attrgetter("id"),
                items="articles",
            ),
            width=2

        ),
        Back(Const("Назад")),
        state=EducationStates.select_article,
        getter=getters.get_articles_to_window
    )