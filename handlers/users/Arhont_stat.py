from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(commands=['Arhont_stat'])
async def bot_pnh(message: types.Message):
    await message.answer(f"заглушка Arhont_stat")
