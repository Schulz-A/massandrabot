from operator import itemgetter
from typing import Text, Union, Sequence, TypeVar, Callable, Any, Dict, Awaitable

from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram_dialog import DialogManager
from aiogram_dialog.dialog import ChatEvent
from aiogram_dialog.widgets.common import ManagedWidget, WhenCondition
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.kbd.select import get_identity
from aiogram_dialog.widgets.widget_event import WidgetEventProcessor, ensure_event_processor

T = TypeVar("T")
TypeFactory = Callable[[str], T]
ItemIdGetter = Callable[[Any], Union[str, int]]
ItemsGetter = Callable[[Dict], Sequence]
OnItemStateChanged = Callable[
    [ChatEvent, ManagedWidget["Select"], DialogManager, str],
    Awaitable,
]
OnItemClick = Callable[
    [CallbackQuery, ManagedWidget["Select"], DialogManager, T],
    Awaitable,
]


class SelectURL(Select):
    def __init__(
            self,
            text: Text,
            url: Text,
            id: str,
            item_id_getter: ItemIdGetter,
            items: Union[str, Sequence],
            type_factory: TypeFactory[T] = str,
            on_click: Union[OnItemClick, WidgetEventProcessor, None] = None,
            when: WhenCondition = None,
    ):
        super().__init__(
            id=id,
            when=when,
            item_id_getter=item_id_getter,
            items=items,
            type_factory=type_factory,
            text=text,
            on_click=on_click
        )

        self.url = url

    async def _render_button(
            self, pos: int, item: Any, data: Dict,
            manager: DialogManager,
    ) -> InlineKeyboardButton:
        data = {"data": data, "item": item, "pos": pos + 1, "pos0": pos}
        item_id = self.item_id_getter(item)
        return InlineKeyboardButton(
            text=await self.text.render_text(data, manager),
            url=await self.url.render_text(data, manager),
        )
