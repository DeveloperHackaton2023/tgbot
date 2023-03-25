from typing import Optional
from dataclasses import dataclass

from aiogram.types import Message

from contrib.handlers.message.context_manager import BaseContextManager, Property
from services.auth import OsiUser


class _Properties:
    message = Property('messsage', Message)
    iin = Property('iin', str)
    phone_number = Property('author', str)
    osi_user = Property('osi_user', OsiUser)


@dataclass
class _RegisterContext:
    message: Optional[_Properties.message.type]
    iin: Optional[_Properties.iin.type]
    phone_number: Optional[_Properties.phone_number.type]
    osi_user: Optional[_Properties.osi_user.type]


class RegisterContextManager(BaseContextManager):
    props: _Properties = _Properties
    _context_type = _RegisterContext

    @property
    def ctx(self) -> _RegisterContext:
        return super().ctx
