from dateutil.parser import parse

from ._types import OsiUser, OsiUserInfo, Flat, Ticket, TicketInfo
from ._base import BaseApiService


class UserService(BaseApiService):
    @classmethod
    def try_get_user_info(cls, user: OsiUser) -> OsiUserInfo:
        input_data = {'iin': user.iin, 'telephone': user.phone_number}
        data = cls._request_api('user/get/info/', input_data)
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
    def _serialize_ticket(cls, data: dict) -> TicketInfo:
        return TicketInfo(
            ticket=Ticket(
                subject=data['subject'],
                description=data['description']
            ),
            created_at=parse(data['created']),
            status=data['statuses'][-1]['title']
        )
