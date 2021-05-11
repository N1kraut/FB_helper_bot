from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            #types.BotCommand("registrate", "Зарегистрироваться"),
            types.BotCommand("Arhont_stat", "Статистика Архонта за неделю"),
            types.BotCommand("Help_fc", "Общедоступная статистика фанфика"),
            types.BotCommand("Help_ar", "Общедоступная статистика автора"),
            #types.BotCommand("exit", "Выйти")
        ]
    )
