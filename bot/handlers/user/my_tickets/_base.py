from contrib.handlers.message.base import BaseHandler as _BaseHandler
from ._context import MyTicketsContextManager


class BaseHandler(MyTicketsContextManager, _BaseHandler):
    pass
