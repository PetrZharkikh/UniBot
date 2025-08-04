from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from utils.gpt import solve_task_with_gpt

router = Router()


class SolveTaskStates(StatesGroup):
    waiting_for_input = State()


@router.callback_query(F.data == "solve_task")
async def start_solve_task(callback: CallbackQuery, state: FSMContext) -> None:
    """Prompt user to enter the task and set FSM state."""
    await callback.message.answer("Please enter your task:")
    await state.set_state(SolveTaskStates.waiting_for_input)
    await callback.answer()


@router.message(SolveTaskStates.waiting_for_input)
async def handle_task_input(message: Message, state: FSMContext) -> None:
    """Process the user's task input and return the solution."""
    solution = await solve_task_with_gpt(message.text)
    await message.answer(solution)
    await state.clear()