from services._types import TicketInfo


class Ticket:
    def __init__(self, info: TicketInfo) -> None:
        self.info = info

    def render(self) -> str:
        text = f'<u>{self.info.ticket.subject}</u>\n'
        text += self.info.ticket.description + '\n'
        text += f'Статус: {self.info.status}'
        return text
