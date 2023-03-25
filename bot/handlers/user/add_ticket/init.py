from typing import Any

from services.auth import AuthService
from ui.components.ticket import TicketForm
from ui.keyboards.flat import user_flats, FlatsMarkup
from ._base import BaseHandler
from ._states import FSM


class InitRegisterHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.delete()
        self.clean_context(exclude=[self.props.osi_user])

        user_info = AuthService.try_get_user_info(self.ctx.osi_user)
        self.set(self.props.user_info, user_info)

        text = TicketForm().render()
        self.set(self.props.message, (await self.event.answer(text)))
        await self.render_widget()
        markup = FlatsMarkup.get_choose_flat_dialog(self.ctx.user_info.flats)
        await self.event.answer('Выберите квартиру', reply_markup=markup)
        await self.state.set_state(FSM.choose_flat)
