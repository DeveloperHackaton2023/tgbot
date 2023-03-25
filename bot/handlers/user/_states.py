from aiogram.fsm.state import State, StatesGroup


class _UserFSM(StatesGroup):
    finish = State()
    show_menu = State()
    check_menu_command = State()


FSM = _UserFSM
