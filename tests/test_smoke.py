from just1kbot import __version__
from just1kbot.main import main


def test_version_present() -> None:
    assert __version__


def test_main_returns_zero() -> None:
    assert main() == 0
