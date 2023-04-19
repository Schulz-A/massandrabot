from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Обучение", callback_data="education")],
        [InlineKeyboardButton(text="Тех. Состояние", callback_data="fixer")]
    ]
)
