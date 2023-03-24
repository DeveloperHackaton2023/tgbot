from typing import Optional

from contrib.handlers.message.context_manager import (
    BaseContextManager, BaseContext
)


class _RegisterContext(BaseContext):
    iin: Optional[int] = None
    phone_number: Optional[str] = None


class RegisterContextManager(BaseContextManager[_RegisterContext]):
    props = _RegisterContext
