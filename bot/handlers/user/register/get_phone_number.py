from typing import Any

from ._base import BaseHandler
from ._states import FSM
from .register import RegisterHandler


class GetPhoneNumberHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)

        phone_number = self.event.contact.phone_number
        self.set(self.props.phone_number, phone_number)

        await RegisterHandler(
            event=self.event,
            state=self.state,
            data=self.user_data
        ).handle()

    @staticmethod
    def _validate_phone_number(self, phone_number: int) -> bool:
        pass  # TODO:
