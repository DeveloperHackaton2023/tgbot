from typing import Any

from ui.keyboards.phone import send_my_number
from ._base import BaseHandler
from ._states import FSM


class GetIinHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)

        iin = int(self.event.text)
        self.set(self.props.iin, iin)

        await self.event.answer(
            'Отправьте ваш номер телефона',
            reply_markup=send_my_number
        )

        await self.state.set_state(FSM.get_phone_number)

    @staticmethod
    def _validate_iin(self, iin: int) -> bool:
        pass  # TODO:
