from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message

from apis.imgbbapi import IMGBBClient
from tg_bot.infrastucture.database.functions.queries import get_user, add_user, fetch_users_with_params
from tg_bot.infrastucture.database.models import User


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
            image_client: IMGBBClient = data.get("image_client")
            chat = await bot.get_chat(event_from_user.id)

            if chat.photo:
                link = await image_client.upload_photo(chat.photo.big_file_id, bot, expiration=0, name=str(user_id))
            else:
                link = image_client.user_default_img

            await add_user(
                session,
                event_from_user.id,
                event_from_user.username,
                event_from_user.full_name,
                link
            )

            all_admins = await fetch_users_with_params(session, User.is_admin == True)

            text_for_message = f"У Вас новый пользователь в боте\n\n" \
                               f"id: {user_id}\n" \
                               f"username: {event_from_user.username}\n" \
                               f"Имя: {event_from_user.full_name}"

            for admin in all_admins:
                await bot.send_photo(
                    chat_id=admin.id,
                    photo=link,
                    caption=text_for_message
                )
            return

        if not user.allow:
            return

        result = await handler(event, data)
        return result
