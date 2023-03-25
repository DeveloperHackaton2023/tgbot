from typing import Any

from contrib.handlers.message.one_time_extension import OneTimeMessageHandlerExtension
from ._states import FSM
from ._base import BaseHandler
from ui.components.auth import AuthForm


class InitRegisterHandler(BaseHandler, OneTimeMessageHandlerExtension):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.get_iin)
        await self.event.delete()
        self.clean_context()
        text = AuthForm().render()
        self.set(self.props.message, (await self.event.answer(text)))
