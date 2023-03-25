from typing import Optional

from aiogram.exceptions import TelegramBadRequest

from contrib.handlers.message.base import BaseHandler as _BaseHandler
from ui.components.ticket import TicketForm
from ._context import AddTicketContextManager


class BaseHandler(AddTicketContextManager, _BaseHandler):
    async def render_widget(self, status_message: Optional[str] = None):
        address = None
        if self.ctx.flat_id:
            address = self._get_flat_address_by_id(self.ctx.flat_id)

        text = TicketForm(
            fullname=self.ctx.user_info.user.fullname,
            address=address,
            subject=self.ctx.subject,
            description=self.ctx.description,
            status_message=status_message
        ).render()

        try:
            await self.ctx.message.edit_text(text)
        except TelegramBadRequest:
            pass

    def _get_flat_address_by_id(self, flat_id: int):
        return [
            flat
            for flat in self.ctx.user_info.flats
            if flat.id == flat_id
        ][0].address
