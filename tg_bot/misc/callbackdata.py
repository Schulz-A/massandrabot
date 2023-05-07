from aiogram.filters.callback_data import CallbackData


class WorkSheetData(CallbackData, prefix="fix"):
    WS_inx: int


class UserData(CallbackData, prefix="user"):
    action: str
    user_id: int
