"""Bot entrypoint."""

import asyncio
import logging

from aiogram import Bot

from app.config import get_settings
from bot.app import create_dispatcher


def configure_logging(level: str) -> None:
    """Configure logging for application startup."""
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO))


async def run() -> None:
    """Run bot polling loop."""
    settings = get_settings()
    configure_logging(settings.app.log_level)

    logger = logging.getLogger(__name__)
    logger.info("Starting bot")

    bot = Bot(token=settings.bot.token.get_secret_value())
    dispatcher = create_dispatcher()

    try:
        await dispatcher.start_polling(bot)
    finally:
        logger.info("Shutting down bot")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(run())
