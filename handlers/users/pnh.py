from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(commands = ['pnh'])
async def bot_pnh(message: types.Message):
    await message.answer(f"пошел нахуй!")
