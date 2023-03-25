from lib.keyboard_builder import KeyboardBuilder


class _Buttons:
    add_ticket = '✉️ Отправить заявку'
    my_tickets = '📨 Мои заявки'


class MenuMarkup:
    buttons = _Buttons

    menu = KeyboardBuilder.add_keyboard(
        buttons=[
            [buttons.add_ticket, buttons.my_tickets]
        ]
    )
