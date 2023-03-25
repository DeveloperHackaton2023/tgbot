from typing import Any

from contrib.handlers.message.one_time_extension import OneTimeMessageHandlerExtension
from ui.components.auth import AuthForm
from ui.keyboards.phone import send_my_number
from ._base import BaseHandler
from ._states import FSM


class GetIinHandler(BaseHandler, OneTimeMessageHandlerExtension):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.delete()

        if not self._validate_iin(self.event.text):
            self._set_one_time_message(
                await self.event.answer('ИИН должен состоять из 12 цифр')
            )
            await self.state.set_state(FSM.get_iin)
            return

        self.set(self.props.iin, self.event.text)

        await self.render_widget()
        self._set_one_time_message(
            await self.event.answer(
                'Отправьте ваш номер телефона',
                reply_markup=send_my_number
            )
        )

        await self.state.set_state(FSM.get_phone_number)

    @staticmethod
    def _validate_iin(iin: str) -> bool:
        for ch in iin:
            if not ch.isdigit():
                return False
        if len(iin) != 12:
            return False
        return True
