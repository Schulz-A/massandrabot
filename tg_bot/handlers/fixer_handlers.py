import asyncio
import datetime
import types

import gspread.utils
from aiogram import F, Router, types, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold
from gspread_asyncio import AsyncioGspreadClientManager, AsyncioGspreadSpreadsheet, AsyncioGspreadWorksheet
from sqlalchemy.ext.asyncio import AsyncSession

from apis.imgbbapi import IMGBBClient
from tg_bot.config import Config
from tg_bot.misc.startkeyboard import fix_menu, close_button, build_project_keyboard

fix_router = Router()


@fix_router.callback_query(F.data == "fixer")
async def start_fix_menu(call: types.CallbackQuery):
    await call.message.answer(
        text=f"Меню технического состояния. Для заполнения формы нажмите {hbold('Заполнить заявку')}",
        reply_markup=fix_menu
    )


@fix_router.callback_query(F.data == "close_fixer")
async def close_fix_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(None)


@fix_router.callback_query(F.data == "start_form")
async def start_form(call: types.CallbackQuery, state: FSMContext):
    edited_message = await call.message.edit_text(
        text="Напишите фамилию и имя",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[close_button]])
    )

    await state.update_data(edited_message=edited_message.message_id)
    await state.set_state("start_form")


@fix_router.message(StateFilter("start_form"))
async def enter_name(message: types.Message, state: FSMContext, session: AsyncSession, bot: Bot):
    data = await state.get_data()
    edited_message = data.get("edited_message")

    name = message.text
    await state.update_data(name=name)

    keyboard = await build_project_keyboard(session)

    edited_message = await bot.edit_message_text(
        text=f"{name}, выбери проект",
        chat_id=message.chat.id,
        message_id=edited_message,
        reply_markup=keyboard.as_markup()
    )

    await state.update_data(edited_message=edited_message.message_id)
    await state.set_state("enter_name")

    await asyncio.sleep(1)
    await message.delete()


@fix_router.callback_query(StateFilter("enter_name"))
async def enter_project(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    name = data.get("name")
    project = call.data

    edited_message = await call.message.edit_text(
        text=f"{name}, опиши проблему",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[close_button]])
    )

    await state.update_data(project=project, edited_message=edited_message.message_id)
    await state.set_state("enter_project")


@fix_router.message(StateFilter("enter_project"))
async def enter_problem(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    edited_message = data.get("edited_message")
    name = data.get("name")
    problem = message.text

    edited_message = await bot.edit_message_text(
        text=f"{name}, пришли фото проблемы",
        chat_id=message.chat.id,
        message_id=edited_message,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[close_button]])
    )

    await state.update_data(problem=problem, edited_message=edited_message.message_id)
    await state.set_state("enter_problem")

    await asyncio.sleep(1)
    await message.delete()


@fix_router.message(StateFilter("enter_problem"))
async def enter_photo(
        message: types.Message,
        state: FSMContext,
        bot: Bot,
        image_client: IMGBBClient,
        google_client_manager: AsyncioGspreadClientManager,
        config: Config
):

    if not message.photo:
        await message.answer("Вы прислали не фото. Попробуйте еще раз")
        return

    data = await state.get_data()
    edited_message = data.get("edited_message")
    date = datetime.datetime.now()
    photo = message.photo[-1]

    await bot.edit_message_text(
        text="Ваша заявка успешно отправлена. Можете закрыть окно",
        chat_id=message.chat.id,
        message_id=edited_message,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Закрыть окно", callback_data="close_fixer")]
            ]
        )
    )

    await asyncio.sleep(1)
    await message.delete()

    photo_url = await image_client.upload_photo(photo, bot, 180, date.date().strftime("%d/%m/%Y"))
    name = data.get("name")
    problem = data.get("problem")
    project = data.get("project")

    google_client = await google_client_manager.authorize()
    spreadsheet = await google_client.open_by_key(config.miscellaneous.spreadsheet_id)
    worksheet = await spreadsheet.get_worksheet(0)
    url = "=IMAGE(\"{}\")".format(photo_url)
    await worksheet.append_row(
        values=[name, project, problem, url, date.date().strftime("%d/%m/%Y")],
        value_input_option=gspread.utils.ValueInputOption.user_entered
    )
