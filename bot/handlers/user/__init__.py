from aiogram import Router

from . import list
from . import register
from . import start


def setup(r: Router):
    list.setup(r)
    start.setup(r)
    register.setup(r)
