from typing import Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass
class OsiUser:
    iin: str
    phone_number: str
    fullname: str


@dataclass
class Ticket:
    subject: str
    description: str


class TicketStatus(Enum):
    CREATED = 'Создано 💾'
    IN_PROGRESS = 'В работе 🔨'
    DENIED = 'Оклонено ❌'
    SUCCESS = 'Выполнено ✅'


@dataclass
class TicketInfo:
    ticket: Ticket
    status: TicketStatus
    admin_response: Optional[str]
    created_at: datetime


@dataclass
class Flat:
    id: int
    address: str
    flat_number: str
    info: str
    tickets: list[TicketInfo]


@dataclass
class OsiUserInfo:
    user: OsiUser
    flats: list[Flat]
