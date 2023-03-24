from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

user_flats = ReplyKeyboardBuilder(
    [
        [KeyboardButton(text='Квартира 1'),
         KeyboardButton(text='Квартира 2')]
    ]
).as_markup(one_time_keyboard=True, resize_keyboard=True)
