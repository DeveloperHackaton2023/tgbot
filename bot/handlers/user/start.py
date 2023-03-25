from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .register.init import InitRegisterHandler
from ._commands import USER_COMMANDS


async def start(message: Message, state: FSMContext, data: dict):
    text = 'Приветствую вас в ОСИ\n\n'
    text += 'Для дальнейшей работы вам необходимо пройти регистрацию\n'
    text += 'Если у вас нет аккаунта обратитесь к администратору вашей ОСИ. '
    text += 'Больше информации вы сможете найти на сайте '
    text += 'https://damirka.space/terricon'
    await message.answer(text)
    await InitRegisterHandler(
        message,
        state=state,
        data=data
    ).handle()


def setup(r: Router):
    r.message.register(start, Command(commands=USER_COMMANDS.start))
