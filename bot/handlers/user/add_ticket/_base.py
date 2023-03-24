from contrib.handlers.message.base import BaseHandler as _BaseHandler
from ._context import AddTicketContextManager


class BaseHandler(AddTicketContextManager, _BaseHandler):
    pass
