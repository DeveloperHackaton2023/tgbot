from typing import Any

from ..menu import show_menu
from ._states import FSM
from ._base import BaseHandler


class RegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.answer('Здравствуйте Балакан Ислам')
        await show_menu(self.event, state=self.state)
