from aiogram.fsm.state import State, StatesGroup


class EducationStates(StatesGroup):
    select_project = State()
    select_category = State()
    select_article = State()
