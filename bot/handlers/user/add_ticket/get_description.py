from typing import Any

from services.auth import Ticket
from services.tickets import TicketsService
from ui.keyboards.menu import MenuMarkup
from .._states import FSM
from ._base import BaseHandler


class GetDescriptionHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        self.set(self.props.description, self.event.text)

        TicketsService.send_ticket(
            self.ctx.user_info.user,
            self.ctx.flat_id,
            Ticket(self.ctx.subject, self.ctx.description)
        )

        await self.event.answer('Ваша заявка отправлена',
                                reply_markup=MenuMarkup.menu)
        await self.state.set_state(FSM.check_menu_command)
