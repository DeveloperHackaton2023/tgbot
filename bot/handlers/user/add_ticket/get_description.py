from typing import Any

from ui.keyboards.menu import MenuMarkup
from .._states import FSM
from ._base import BaseHandler


class GetDescriptionHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.answer('Ваша заявка отправлена',
                                reply_markup=MenuMarkup.menu)
        await self.state.set_state(FSM.check_menu_command)
