from bot.app import create_dispatcher
from bot.main import run


def test_create_dispatcher() -> None:
    dispatcher = create_dispatcher()
    assert dispatcher is not None


def test_bot_entrypoint_import_smoke() -> None:
    assert callable(run)
