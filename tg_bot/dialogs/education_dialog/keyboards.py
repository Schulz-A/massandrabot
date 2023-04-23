import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select
from aiogram_dialog.widgets.text import Format


def paginated_projects(on_click):
    return ScrollingGroup(
        Select(
            Format("{item.name}"),
            id="projects_group",
            item_id_getter=operator.attrgetter("id"),
            items="projects",
            on_click=on_click
        ),
        id="scrolling_projects",
        width=1, height=4
    )
