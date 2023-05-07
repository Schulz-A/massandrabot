from aiogram import Router, types, Bot, F
from aiogram.filters import StateFilter
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.infrastucture.database.functions.queries import update_user, delete_user
from tg_bot.infrastucture.database.models import User
from tg_bot.misc.callbackdata import UserData

new_user_router = Router()


@new_user_router.callback_query(UserData.filter(F.action == "accept"))
async def accept_new_user(call: types.CallbackQuery, callback_data: UserData, bot: Bot, session: AsyncSession):
    await update_user(session, User.id == callback_data.user_id, allow=True)
    await bot.send_message(
        chat_id=callback_data.user_id,
        text="Вам был предоставлен доступ к боту\n"
             "Нажмите на команду /start"
    )

    await call.answer("Пользователю разрешен доступ!", show_alert=True)
    await call.message.delete()


@new_user_router.callback_query(UserData.filter(F.action == "cancel"))
async def cancel(call: types.CallbackQuery):
    text = "Вы отменили заявку пользователя. " \
           "Предоставить доступ и просмотреть информацию о нем вы все еще можете в панели администратора"

    await call.answer(text=text, show_alert=True)
    await call.message.delete()


@new_user_router.callback_query(UserData.filter(F.action == "delete"))
async def delete_new_user(call: types.CallbackQuery, session: AsyncSession, callback_data: UserData):
    await delete_user(session, User.id == callback_data.user_id)

    await call.answer("Пользователь удален из базы данных", show_alert=True)
    await call.message.delete()
