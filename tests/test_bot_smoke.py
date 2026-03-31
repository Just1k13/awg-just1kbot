from bot.app import create_dispatcher


def test_create_dispatcher() -> None:
    dispatcher = create_dispatcher()
    assert dispatcher is not None
