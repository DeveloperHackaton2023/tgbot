from aiogram import Router, F
from aiogram.filters import StateFilter, and_f, invert_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from ui.keyboards.menu import MenuMarkup
from ._states import FSM
from .add_ticket.init import InitRegisterHandler


async def show_menu(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в ОСИ',
                         reply_markup=MenuMarkup.menu)
    await state.set_state(FSM.check_menu_command)


async def check_menu_command(message: Message, state: FSMContext, data: dict):
    match message.text:
        case MenuMarkup.buttons.add_ticket:
            await InitRegisterHandler(message, state=state, data=data)
        case 'q':
            await state.set_state(FSM.finish)
            await message.answer('Пока', reply_markup=ReplyKeyboardRemove())
        case _:
            await state.set_state(FSM.check_menu_command)


def setup(r: Router):
    r.message.register(show_menu, and_f(
        StateFilter(FSM.show_menu),
        invert_f(F.text.startswith('/'))
    ))
    r.message.register(
        check_menu_command,
        StateFilter(FSM.check_menu_command)
    )
