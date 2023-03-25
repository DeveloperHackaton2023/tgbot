import requests

from settings import API_URL
from .auth import Ticket, OsiUser, ApiRequestFailed


class TicketsService:
    @classmethod
    def send_ticket(cls, user: OsiUser, flat_id: int, ticket: Ticket) -> None:
        input_data = {
            "iin": user.iin,
            "telephone": user.phone_number,
            "houseId": flat_id,
            "subject": ticket.subject,
            "description": ticket.description
        }
        try:
            response = requests.post(
                API_URL + 'user/add/ticket/', json=input_data)
            if response.status_code != 200:
                raise ApiRequestFailed
        except Exception as e:
            print(e)
            raise ApiRequestFailed
