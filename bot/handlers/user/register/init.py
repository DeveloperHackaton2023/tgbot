from typing import Any

from ._base import BaseHandler
from ._states import FSM


class InitRegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.answer('Введите ваш ИИН')
        await self.state.set_state(FSM.get_iin)
