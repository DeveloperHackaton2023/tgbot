from typing import Any

from ._base import BaseHandler
from ._states import FSM


class GetDescriptionHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.answer('Ваша заявка отправлена')
