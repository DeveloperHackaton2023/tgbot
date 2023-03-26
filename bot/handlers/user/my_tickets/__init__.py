from aiogram import Router
from aiogram.filters import Command

from .._commands import USER_COMMANDS
from .my_tickets import MyTicketsHandler


def setup(r: Router):
    r.message.register(MyTicketsHandler, Command(
        commands=USER_COMMANDS.my_tickets))
