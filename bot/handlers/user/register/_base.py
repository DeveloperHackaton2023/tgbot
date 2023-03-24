from contrib.handlers.message.base import BaseHandler as _BaseHandler
from ._context import RegisterContextManager


class BaseHandler(RegisterContextManager, _BaseHandler):
    pass
