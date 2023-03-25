from dataclasses import dataclass
from datetime import datetime


@dataclass
class OsiUser:
    iin: str
    phone_number: str
    fullname: str


@dataclass
class Ticket:
    subject: str
    description: str


@dataclass
class TicketInfo:
    ticket: Ticket
    status: str
    created_at: datetime


@dataclass
class Flat:
    id: int
    address: str
    info: str
    tickets: list[TicketInfo]


@dataclass
class OsiUserInfo:
    user: OsiUser
    flats: list[Flat]
