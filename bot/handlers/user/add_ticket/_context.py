from typing import Optional
from dataclasses import dataclass

from contrib.handlers.message.context_manager import BaseContextManager, Property
from services.auth import OsiUser


class _Properties:
    iin = Property('iin', str)
    phone_number = Property('author', str)
    osi_user = Property('osi_user', OsiUser)


@dataclass
class _AddTicketContext:
    iin: Optional[_Properties.iin.type]
    phone_number: Optional[_Properties.phone_number.type]
    osi_user: Optional[_Properties.osi_user.type]


class AddTicketContextManager(BaseContextManager):
    props: _Properties = _Properties
    _context_type = _AddTicketContext

    @property
    def ctx(self) -> _AddTicketContext:
        return super().ctx
