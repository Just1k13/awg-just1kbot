"""Typed application settings loaded from environment."""

from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    """Telegram bot settings."""

    token: SecretStr = Field(..., description="Telegram bot token")


class DatabaseSettings(BaseSettings):
    """Database settings."""

    dsn: str = Field(..., description="SQLAlchemy DSN for PostgreSQL")
    echo: bool = False


class AppRuntimeSettings(BaseSettings):
    """General application runtime settings."""

    log_level: str = "INFO"


class Settings(BaseSettings):
    """Top-level settings container."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_prefix="",
        extra="ignore",
    )

    bot: BotSettings
    db: DatabaseSettings
    app: AppRuntimeSettings = AppRuntimeSettings()


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache settings."""
    return Settings()
