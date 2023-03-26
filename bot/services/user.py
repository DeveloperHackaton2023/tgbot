from dateutil.parser import parse
from typing import Optional

from ._types import OsiUser, OsiUserInfo, Flat, Ticket, TicketInfo, TicketStatus
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
        info = data['info']
        if not data['info']:
            info = ''
        return Flat(
            id=data['id'],
            address=data['address'],
            info=info,
            flat_number=data['flatNumber'],
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
            status=cls._serialize_status(data['statuses'][-1]['title']),
            admin_response=cls._serialize_admin_response(data['adminResponse'])
        )

    @classmethod
    def _serialize_status(cls, status: str) -> TicketStatus:
        match status:
            case 'Created':
                return TicketStatus.CREATED
            case 'InProgress':
                return TicketStatus.IN_PROGRESS
            case 'Denied':
                return TicketStatus.DENIED
            case 'Success':
                return TicketStatus.SUCCESS
            case _:
                raise ValueError

    @classmethod
    def _serialize_admin_response(cls, resp: str) -> Optional[str]:
        if resp == 'Null':
            return None
        return resp

