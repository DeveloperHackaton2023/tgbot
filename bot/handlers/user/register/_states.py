from aiogram.fsm.state import State, StatesGroup


class _RegisterFSM(StatesGroup):
    init = State()
    get_iin = State()
    get_phone_number = State()
    finish = State()


FSM = _RegisterFSM
