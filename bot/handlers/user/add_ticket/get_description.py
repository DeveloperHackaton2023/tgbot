from typing import Any

from services._exceptions import ApiRequestFailed
from services._types import Ticket
from services.tickets import TicketsService
from .._states import FSM
from ._base import BaseHandler


class GetDescriptionHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.delete()
        self.set(self.props.description, self.event.text)
        await self.render_widget()

        try:
            TicketsService.send_ticket(
                self.ctx.user_info.user,
                self.ctx.flat_id,
                Ticket(self.ctx.subject, self.ctx.description)
            )
            status_message = '<b><u>Успешно отправлено</u></b> ✅'
        except ApiRequestFailed:
            status_message = '<b><u>Не получилось отправить</u></b> ❌'

        await self.render_widget(status_message)
        await self.state.set_state(FSM.check_menu_command)
