from typing import Any

from contrib.handlers.callback.base import BaseHandler as _BaseHandler
from ._base import BaseHandler
from ._states import FSM


class ChooseFlatHandler(_BaseHandler, BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.message.delete()
        flat_id = self.event.data.split(':')[1]
        self.set(self.props.flat_id, int(flat_id))
        await self.render_widget()
        await self.state.set_state(FSM.get_subject)
