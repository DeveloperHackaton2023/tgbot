from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

send_my_number = ReplyKeyboardBuilder(
    [
        [KeyboardButton(text='Оправить номер', request_contact=True)]
    ]
).as_markup(one_time_keyboard=True, resize_keyboard=True)
