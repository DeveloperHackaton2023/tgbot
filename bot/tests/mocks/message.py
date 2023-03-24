from unittest.mock import MagicMock, AsyncMock

from aiogram.types import CallbackQuery, User

fake_event = AsyncMock()


def make_fake_callback(data: str) -> CallbackQuery:
    return CallbackQuery(
        from_user=User(id=1, is_bot=False, first_name='user'),
        id=1,
        chat_instance='1',
        data=data
    )
