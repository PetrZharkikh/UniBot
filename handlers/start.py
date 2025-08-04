from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Handle the /start command."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🧮 Solve a task", callback_data="solve_task")
    builder.button(text="📑 Generate PDF", callback_data="generate_pdf")
    builder.adjust(1)

    welcome_text = (
        "👋 Hi! I'm UniHelperBot — your personal academic assistant.\n\n"
        "I can help you:\n"
        "🧮 Solve math, physics, or theory tasks  \n"
        "📑 Write short texts and turn them into PDFs  \n\n"
        "Choose an option below to get started:"
    )

    await message.answer(welcome_text, reply_markup=builder.as_markup())