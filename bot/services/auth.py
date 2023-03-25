from dataclasses import dataclass
import json

import requests

from settings import API_URL


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
class Flat:
    id: int
    address: str
    info: str
    tickets: list[Ticket]


@dataclass
class OsiUserInfo:
    user: OsiUser
    flats: list[Flat]


class AuthService:
    @classmethod
    def try_get_user(cls, iin: int, phone_number: str) -> OsiUser:
        input_data = {'iin': str(iin), 'telephone': phone_number}
        user_info = requests.post(API_URL + 'user/get/info/', json=input_data)
        data = json.loads(user_info.text)
        return OsiUser(
            iin=data['iin'],
            phone_number=data['telephone'],
            fullname=data['fullname']
        )

    @classmethod
    def try_get_user_info(cls, user: OsiUser) -> OsiUserInfo:
        input_data = {'iin': user.iin, 'telephone': user.phone_number}
        user_info = requests.post(API_URL + 'user/get/info/', json=input_data)
        data = json.loads(user_info.text)
        return OsiUserInfo(
            user=user,
            flats=[cls._serialize_flat(flat) for flat in data['houses']]
        )

    @classmethod
    def _serialize_flat(cls, data: dict) -> Flat:
        return Flat(
            id=data['id'],
            address=data['address'],
            info=data['info'],
            tickets=[cls._serialize_ticket(t) for t in data['tickets']]
        )

    @classmethod
    def _serialize_ticket(cls, data: dict) -> Ticket:
        return Ticket(
            subject=data['subject'],
            description=data['description']
        )