from typing import Optional, Any

from .base import BaseComponent


class AuthForm(BaseComponent):
    def __init__(
        self,
        iin: Optional[int] = None,
        phone_number: Optional[str] = None,
        status_message: Optional[str] = None
    ) -> None:
        if iin:
            self.iin = str(iin)
        else:
            self.iin = None
        self.phone_number = phone_number
        self.status_message = status_message
        self.__has_highlighted_property = False

    def render(self) -> str:
        text = '<u>Аутэнтификация 👤</u>\n'
        text += self.__render_property(self.iin, prefix='ИИН: ')
        text += self.__render_property(self.phone_number, prefix='Телефон: ')
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
