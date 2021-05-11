from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    sti = open('other/stickers/hello.webp', 'rb')

    await message.answer_sticker(sti)
    await message.answer(f"Привет, фикрайдер, {message.from_user.full_name}!\nЯ - <b>Фикбуковский Помощник</b>, бот созданный, что бы помочь тебе собрать некоторую статистику на фикбуке.",parse_mode='html')
