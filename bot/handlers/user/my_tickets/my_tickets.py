from typing import Any
import asyncio

from services.tickets import TicketsService
from ui.widgets.ticket import Ticket
from .._states import FSM
from ._base import BaseHandler


class MyTicketsHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.event.answer('Ваши заявки: ')
        tickets = TicketsService.get_user_tickets(self.ctx.osi_user)
        for ticket in tickets:
            text = Ticket(ticket).render()
            await asyncio.sleep(0.1)
            await self.event.answer(text)
        await self.state.set_state(FSM.check_menu_command)
