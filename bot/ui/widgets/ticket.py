from services._types import TicketInfo


class Ticket:
    def __init__(self, info: TicketInfo) -> None:
        self.info = info

    def render(self) -> str:
        text = f'<b>{self.info.ticket.subject}</b>\n'
        # text += self.info.ticket.description + '\n\n'
        if self.info.admin_response:
            text += f'<u>Ответ администратора:</u> {self.info.admin_response}\n'
        text += f'<u>Статус:</u> <b>{self.info.status.value}</b>'
        return text
