from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"<b>Привет {message.from_user.first_name}. Рад тебя видеть !</b>"
    )
