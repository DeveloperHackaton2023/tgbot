from aiogram import Router

from . import list


def setup(r: Router):
    list.setup(r)
