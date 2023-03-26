from lib.commands import Commands as _Commands


class _UserCommands(_Commands):
    list = 'list'
    start = 'start'
    register = 'register'
    add_ticket = 'add_ticket'
    my_tickets = 'my_tickets'


USER_COMMANDS = _UserCommands()
