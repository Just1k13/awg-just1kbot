"""Public bot handlers."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="public")


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    """Handle /start command."""
    await message.answer("Hello! Foundation mode is active. Features will arrive in small PRs.")


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    """Handle /help command."""
    await message.answer("Available commands: /start, /help")
