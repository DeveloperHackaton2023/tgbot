from typing import Any

from ._base import BaseHandler
from ._states import FSM


class GetSubjectHandler(BaseHandler):
    async def handle(self) -> Any:
        await self.state.set_state(FSM.finish)
        await self.event.delete()
        self.set(self.props.subject, self.event.text)
        await self.render_widget()
        await self.state.set_state(FSM.get_description)
