from aiogram.filters.callback_data import CallbackData


class WorkSheetData(CallbackData, prefix="fix"):
    WS_inx: int
