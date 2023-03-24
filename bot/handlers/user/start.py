from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ._commands import USER_COMMANDS


async def start(message: Message):
    text = 'Приветствую вас в ОСИ /list для списка комманд\n\n'
    text += '/register для регистрации'
    await message.answer(text)


def setup(r: Router):
    r.message.register(start, Command(commands=USER_COMMANDS.start))
