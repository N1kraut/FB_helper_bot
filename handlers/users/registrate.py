from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command(['registrate']))
async def bot_pnh(message: types.Message):
    await message.answer(f"заглушка регистрации")
