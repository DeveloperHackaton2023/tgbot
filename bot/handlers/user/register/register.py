from typing import Any

from services.auth import AuthService, ApiRequestFailed
from ..menu import show_menu
from ._states import FSM
from ._base import BaseHandler


class RegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)

        try:
            user = AuthService.try_get_user(
                iin=self.ctx.iin, phone_number=self.ctx.phone_number)
            self.set(self.props.osi_user, user)
            status_message = f'<u>Авторизовано:</u> <b>{user.fullname}</b> ✅'
            await self.render_widget(status_message)
            await show_menu(self.event, state=self.state)
        except ApiRequestFailed:
            status_message = '<u>Проверьте корректность введенных данных</u> ❌'
            await self.render_widget(status_message)
            await self.event.answer('/register для повторной попытки')
