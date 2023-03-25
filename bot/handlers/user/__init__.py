from aiogram import Router

from . import list
from . import register
from . import start
from . import add_ticket
from . import menu


def setup(r: Router):
    list.setup(r)
    start.setup(r)
    register.setup(r)
    add_ticket.setup(r)
    menu.setup(r)
