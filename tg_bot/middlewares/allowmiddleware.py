from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import BufferedInputFile, Message, InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.infrastucture.database.functions.queries import (
    add_user, fetch_users_with_params, get_user)
from tg_bot.infrastucture.database.models import User
from tg_bot.misc.callbackdata import UserData


class AllowMiddleWare(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        event_from_user = data.get("event_from_user")
        session = data.get("session")

        user_id = event_from_user.id
        user = await get_user(session, User.id == user_id)

        if not user:
            bot: Bot = data.get("bot")
            chat = await bot.get_chat(event_from_user.id)

            if chat.photo:
                path = f"users_photo/{user_id}.jpg"
                await bot.download(chat.photo.big_file_id, path)
            else:
                path = "users_photo/question_mark.jpg"

            await add_user(
                session,
                event_from_user.id,
                event_from_user.username,
                event_from_user.full_name,
                path
            )

            all_admins = await fetch_users_with_params(session, User.is_admin == True)  # noqa:E712

            text_for_message = f"У Вас новый пользователь в боте\n\n" \
                               f"id: {user_id}\n" \
                               f"username: {event_from_user.username}\n" \
                               f"Имя: {event_from_user.full_name}"

            photo = BufferedInputFile.from_file(path, str(user_id))

            for admin in all_admins:
                await bot.send_photo(
                    chat_id=admin.id,
                    photo=photo,
                    caption=text_for_message,
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(
                                    text="Разрешить доступ пользователю",
                                    callback_data=UserData(user_id=user_id, action="accept").pack()
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text="Отменить",
                                    callback_data=UserData(user_id=user_id, action="cancel").pack()
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text="Удалить пользователя",
                                    callback_data=UserData(user_id=user_id, action="delete").pack()
                                )
                            ]
                        ]
                    )
                )
            return

        if not user.allow:
            return

        result = await handler(event, data)
        return result
