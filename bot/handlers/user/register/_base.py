from typing import Optional

from aiogram.exceptions import TelegramBadRequest

from contrib.handlers.message.base import BaseHandler as _BaseHandler
from ui.components.auth import AuthForm
from ._context import RegisterContextManager


class BaseHandler(RegisterContextManager, _BaseHandler):
    async def render_widget(self, status_message: Optional[str] = None):
        text = AuthForm(
            iin=self.ctx.iin,
            phone_number=self.ctx.phone_number,
            status_message=status_message
        ).render()

        try:
            await self.ctx.message.edit_text(text)
        except TelegramBadRequest:
            pass
