from typing import Optional
from dataclasses import dataclass

from contrib.handlers.message.context_manager import BaseContextManager, Property
from services._types import OsiUser


class _Properties:
    osi_user = Property('osi_user', OsiUser)


@dataclass
class _MyTicketsContext:
    osi_user: Optional[_Properties.osi_user.type]


class MyTicketsContextManager(BaseContextManager):
    props: _Properties = _Properties
    _context_type = _MyTicketsContext

    @property
    def ctx(self) -> _MyTicketsContext:
        return super().ctx
