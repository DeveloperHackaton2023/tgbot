from aiogram import Router

from . import list
from . import register
from . import start
from . import add_ticket


def setup(r: Router):
    list.setup(r)
    start.setup(r)
    register.setup(r)
    add_ticket.setup(r)
