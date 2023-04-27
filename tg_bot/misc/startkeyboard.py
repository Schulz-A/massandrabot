from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.infrastucture.database.functions.queries import get_projects

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Обучение 📖", callback_data="education")],
        [InlineKeyboardButton(text="Тех. Состояние 🛠️", callback_data="fixer")],
        [InlineKeyboardButton(text="Админ Панель 🎛️", callback_data="admin_panel")]
    ]
)

close_button = InlineKeyboardButton(text="Закрыть", callback_data="close_fixer")

fix_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Заполнить заявку", callback_data="start_form")],
        [close_button]
    ]
)


async def build_project_keyboard(session: AsyncSession) -> InlineKeyboardBuilder:
    projects = await get_projects(session)
    builder = InlineKeyboardBuilder()

    for project in projects:
        builder.button(text=f"{project.name}", callback_data=f"{project.name}")

    builder.adjust(2)
    builder.row(close_button, width=1)

    return builder
