from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("filltables", "Заполнить таблицы"),
            #types.BotCommand("temp", ""),
            #types.BotCommand("registrate", "Зарегистрироваться"),
            #types.BotCommand("arhont_stat", "Статистика Архонта за неделю"),
            #types.BotCommand("help_fc", "Общедоступная статистика фанфика"),
            #types.BotCommand("help_ar", "Общедоступная статистика автора"),
            #types.BotCommand("exit", "Выйти")
        ]
    )
