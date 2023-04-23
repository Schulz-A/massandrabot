from aiogram.fsm.state import StatesGroup, State


class EducationStates(StatesGroup):
    select_project = State()
    select_category = State()
    select_article = State()
