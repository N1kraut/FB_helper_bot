from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



"""
choise = InlineKeyboardMarkup(
    inline_keyboard=[

            InlineKeyboardButton(text="Показать фанфики, которые появились в топе сегодня", callback_data=saw_names(0)),
            InlineKeyboardButton(text="Показать фанфики, которые появились в топе гет за сегодня", callback_data=saw_names(1)),
            InlineKeyboardButton(text="Показать фанфики, которые появились в топе джен за сегодня", callback_data=saw_names(2))

    ]
)
"""

choise = InlineKeyboardMarkup(row_width=3)

ce_all = InlineKeyboardButton(text="Все", callback_data="top_all")
choise.insert(ce_all)

ce_het = InlineKeyboardButton(text="Джен", callback_data="top_gen")
choise.insert(ce_het)

ce_gen= InlineKeyboardButton(text="Гет", callback_data="top_het")
choise.insert(ce_gen)
