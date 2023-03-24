from aiogram import Router
from aiogram.filters import Command, StateFilter

from .._commands import USER_COMMANDS
from ._states import FSM
from .init import InitRegisterHandler
from .get_iin import GetIinHandler
from .get_phone_number import GetPhoneNumberHandler


def setup(r: Router):
    r.message.register(InitRegisterHandler, Command(
        commands=USER_COMMANDS.register))
    r.message.register(GetIinHandler, StateFilter(FSM.get_iin))
    r.message.register(GetPhoneNumberHandler,
                       StateFilter(FSM.get_phone_number))
