from aiogram import Router, F, types

fix_router = Router()


@fix_router.callback_query(F.data == "fixer")
async def start_fix_menu(call: types.CallbackQuery):
    await call.message.answer("ПЕТУХ")
