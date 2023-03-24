from aiogram.fsm.state import State, StatesGroup


class _AddTicketFsm(StatesGroup):
    finish = State()
    choose_flat = State()
    get_subject = State()
    get_description = State()


FSM = _AddTicketFsm
