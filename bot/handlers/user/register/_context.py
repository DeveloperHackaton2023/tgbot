from typing import Optional
from dataclasses import dataclass

from aiogram.types import Message

from contrib.handlers.message.context_manager import BaseContextManager, Property


class _Properties:
    message = Property('messsage', Message)
    iin = Property('iin', int)
    phone_number = Property('author', str)


@dataclass
class _RegisterContext:
    message: Optional[_Properties.message.type]
    iin: Optional[_Properties.iin.type]
    phone_number: Optional[_Properties.phone_number.type]


class RegisterContextManager(BaseContextManager):
    props: _Properties = _Properties
    _context_type = _RegisterContext

    @property
    def ctx(self) -> _RegisterContext:
        return super().ctx
