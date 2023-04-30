import operator

from aiogram_dialog.widgets.kbd import Group, Select
from aiogram_dialog.widgets.text import Format


def paginated_projects(on_click):
    return Group(
        Select(
            Format("{item.name}"),
            id="projects_group",
            item_id_getter=operator.attrgetter("id"),
            items="projects",
            on_click=on_click
        ),
        width=1
    )
