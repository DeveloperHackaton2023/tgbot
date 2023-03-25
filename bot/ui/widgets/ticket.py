from services._types import TicketInfo


class Ticket:
    def __init__(self, info: TicketInfo) -> None:
        self.info = info

    def render(self) -> str:
        text = f'<b>{self.info.ticket.subject}</b>\n'
        # text += self.info.ticket.description + '\n\n'
        text += f'Статус: {self.info.status.value}'
        return text
