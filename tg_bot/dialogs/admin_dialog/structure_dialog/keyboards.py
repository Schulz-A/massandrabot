import operator

from aiogram_dialog.widgets.kbd import Group, Select
from aiogram_dialog.widgets.text import Format


def column_select(on_click):
    return Group(
        Select(
            Format("{item[0]}"),
            id="column_group",
            item_id_getter=operator.itemgetter(1),
            items="coll_names",
            on_click=on_click
        ),
        width=2
    )
