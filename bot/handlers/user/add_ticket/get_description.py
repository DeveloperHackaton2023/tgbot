from typing import Any

from services.auth import Ticket
from services.tickets import TicketsService
from ui.keyboards.menu import MenuMarkup
from .._states import FSM
from ._base import BaseHandler


class GetDescriptionHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.delete()
        self.set(self.props.description, self.event.text)
        await self.render_widget()

        TicketsService.send_ticket(
            self.ctx.user_info.user,
            self.ctx.flat_id,
            Ticket(self.ctx.subject, self.ctx.description)
        )

        await self.render_widget('<b><u>Успешно отправлено</u></b> ✅')
        await self.state.set_state(FSM.check_menu_command)
