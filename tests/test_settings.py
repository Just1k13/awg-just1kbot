import pytest

from app.config.settings import Settings


def test_settings_load_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT__TOKEN", "123456:token")
    monkeypatch.setenv("DB__DSN", "postgresql+asyncpg://u:p@localhost:5432/test")
    monkeypatch.setenv("APP__LOG_LEVEL", "DEBUG")

    settings = Settings()

    assert settings.bot.token.get_secret_value() == "123456:token"
    assert settings.db.dsn.endswith("/test")
    assert settings.app.log_level == "DEBUG"
