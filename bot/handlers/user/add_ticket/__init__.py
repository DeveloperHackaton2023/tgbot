from aiogram import Router
from aiogram.filters import Command, StateFilter

from .._commands import USER_COMMANDS
from ._states import FSM
from .init import InitRegisterHandler
from .choose_flat import ChooseFlatHandler
from .get_subject import GetSubjectHandler
from .get_description import GetDescriptionHandler


def setup(r: Router):
    r.message.register(InitRegisterHandler, Command(
        commands=USER_COMMANDS.add_ticket))
    r.message.register(ChooseFlatHandler, StateFilter(FSM.choose_flat))
    r.message.register(GetDescriptionHandler, StateFilter(FSM.get_description))
    r.message.register(GetSubjectHandler, StateFilter(FSM.get_subject))
