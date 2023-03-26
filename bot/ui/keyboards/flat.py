from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

from services._types import Flat

user_flats = ReplyKeyboardBuilder(
    [
        [KeyboardButton(text='Квартира 1'),
         KeyboardButton(text='Квартира 2')]
    ]
).as_markup(one_time_keyboard=True, resize_keyboard=True)


class FlatsMarkup:
    prefix = 'flt'

    @classmethod
    def get_choose_flat_dialog(cls, flats: list[Flat]):
        return InlineKeyboardBuilder(
            [
                [
                    InlineKeyboardButton(
                        text=flat.address + ' : ' + flat.flat_number,
                        callback_data=f'{cls.prefix}:{flat.id}'
                    )
                ]
                for flat in flats
            ]
        ).as_markup()
