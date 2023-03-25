from typing import Optional
from dataclasses import dataclass

from contrib.handlers.message.context_manager import BaseContextManager, Property
from services.auth import OsiUser, OsiUserInfo, Flat


class _Properties:
    osi_user = Property('osi_user', OsiUser)
    user_info = Property('user_info', OsiUserInfo)
    flat_id = Property('flat_id', int)
    subject = Property('subject', str)
    description = Property('description', str)


@dataclass
class _AddTicketContext:
    osi_user: Optional[_Properties.osi_user.type]
    user_info: Optional[_Properties.user_info.type]
    flat_id: Optional[_Properties.flat_id.type]
    subject: Optional[_Properties.subject.type]
    description: Optional[_Properties.description.type]


class AddTicketContextManager(BaseContextManager):
    props: _Properties = _Properties
    _context_type = _AddTicketContext

    @property
    def ctx(self) -> _AddTicketContext:
        return super().ctx
