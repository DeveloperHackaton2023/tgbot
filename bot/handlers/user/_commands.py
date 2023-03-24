from lib.commands import Commands as _Commands


class _UserCommands(_Commands):
    list = 'list'


USER_COMMANDS = _UserCommands()
