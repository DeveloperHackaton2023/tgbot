from typing import Any

from services.auth import AuthService
from ..menu import show_menu
from ._states import FSM
from ._base import BaseHandler


class RegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        user = AuthService.try_get_user(
            iin=self.ctx.iin, phone_number=self.ctx.phone_number)
        self.set(self.props.osi_user, user)
        await self.render_widget(f'Авторизовано: {user.fullname} ✅')
        await show_menu(self.event, state=self.state)
