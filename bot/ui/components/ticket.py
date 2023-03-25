from typing import Optional, Any

from .base import BaseComponent


class TicketForm(BaseComponent):
    def __init__(
        self,
        fullname: Optional[str] = None,
        address: Optional[str] = None,
        subject: Optional[str] = None,
        description: Optional[str] = None,
        status_message: Optional[str] = None
    ) -> None:
        self.fullname = fullname
        self.address = address
        self.subject = subject
        self.description = description
        self.status_message = status_message
        self.__has_highlighted_property = False

    def render(self) -> str:
        text = '<u>Заявка ✉️</u>\n'
        text += self.__render_property(self.fullname, prefix='От: ')
        text += self.__render_property(self.address, prefix='Квартира: ')
        text += self.__render_property(self.subject, prefix='Тема: ')
        text += self.__render_property(self.description, prefix='Описание: ')
        text += self._render_if_exist(self.status_message)
        return text

    def __render_property(self, prop: Any, prefix: str = '',
                          new_line: bool = True) -> str:
        highlight = self._is_property_not_exist(prop) \
            and not self.__has_highlighted_property
        text = self._highlight_if(
            highlight, prefix + self._render_if_exist(prop, '... '))
        if new_line:
            text += '\n'

        if highlight:
            self.__has_highlighted_property = True

        return text
