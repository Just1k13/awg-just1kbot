"""Bot application assembly helpers."""

from aiogram import Dispatcher

from bot.handlers import router


def create_dispatcher() -> Dispatcher:
    """Create dispatcher and include root routers."""
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    return dispatcher
