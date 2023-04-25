from aiogram_dialog import DialogManager

from tg_bot.infrastucture.database.functions.queries import get_user, get_users
from tg_bot.infrastucture.database.models import User


async def get_users_to_window(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    users = await get_users(session)

    data = {
        "users": users
    }

    return data


async def get_user_info(dialog_manager: DialogManager, **middleware_data):
    session = middleware_data.get("session")
    user_id = dialog_manager.dialog_data.get("user_id")
    user: User = await get_user(session, User.id == user_id)

    dialog_manager.dialog_data.update(allow=user.allow)
    dialog_manager.dialog_data.update(is_admin=user.is_admin)
    dialog_manager.dialog_data.update(full_name=user.full_name)

    data = {
        "full_name": user.full_name,
        "path": user.photo_path,
        "id": user.id,
        "allow": "Разрешен" if user.allow else "Запрещен",
        "is_admin": "Да" if user.is_admin else "Нет"
    }

    return data


async def get_deleting_user(dialog_manager: DialogManager, **middleware_data):
    # print(dialog_manager.dialog_data)
    full_name = dialog_manager.dialog_data.get("full_name")

    data = {
        "full_name": full_name
    }

    return data
