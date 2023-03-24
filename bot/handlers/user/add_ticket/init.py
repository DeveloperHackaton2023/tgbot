from typing import Any

from ui.keyboards.flat import user_flats
from ._base import BaseHandler
from ._states import FSM


class InitRegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.answer('Выберите квартиру', reply_markup=user_flats)
        await self.state.set_state(FSM.choose_flat)
