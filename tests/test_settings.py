import pytest

from app.config.settings import Settings


def test_settings_load_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT_TOKEN", "123456:token")
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://u:p@localhost:5432/test")
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("DEBUG", "true")

    settings = Settings()

    assert settings.bot.token.get_secret_value() == "123456:token"
    assert settings.db.dsn.endswith("/test")
    assert settings.app.env == "test"
    assert settings.app.debug is True
