from typing import Optional

from contrib.handlers.message.context_manager import (
    BaseContext, BaseContextManager
)


class _AddTicketContext(BaseContext):
    flat_id: Optional[int] = None
    iin: Optional[int] = None
    phone: Optional[str] = None
    subject: Optional[int] = None
    description: Optional[int] = None


class AddTicketContextManager(BaseContextManager[_AddTicketContext]):
    props = _AddTicketContext
