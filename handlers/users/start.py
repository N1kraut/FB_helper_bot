from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.inline import choise_buttons

from utils.parsing.FB_parcer import saw_names

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    sti = open('other/stickers/hello.webp', 'rb')

    await message.answer_sticker(sti)
    await message.answer(f"Привет, фикрайдер, {message.from_user.full_name}!\nЯ - <b>Фикбуковский Помощник</b>, бот созданный, что бы помочь тебе собрать некоторую статистику на фикбуке.",parse_mode='html', reply_markup=choise_buttons.choise)

@dp.callback_query_handler(text_contains="top_all")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("НОВЫЕ ФАНФИКИ В РАЗДЕЛЕ 'all'")
    mass = saw_names(0)
    for names in mass:
        await call.message.answer(f"Name: '{names[0]}' \n URL: {names[1]}")

@dp.callback_query_handler(text_contains="top_gen")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("НОВЫЕ ФАНФИКИ В РАЗДЕЛЕ 'gen'")
    mass = saw_names(1)
    for names in mass:
        await call.message.answer(f"Name: '{names[0]}' \n URL: {names[1]}")

@dp.callback_query_handler(text_contains="top_het")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("НОВЫЕ ФАНФИКИ В РАЗДЕЛЕ 'het'")
    mass = saw_names(2)
    for names in mass:
        await call.message.answer(f"Name: '{names[0]}' \n URL: {names[1]}")
