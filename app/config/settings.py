"""Typed application settings loaded from environment."""

from functools import lru_cache

from pydantic import Field, SecretStr, model_validator
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

    env: str = "dev"
    debug: bool = False
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

    @model_validator(mode="before")
    @classmethod
    def map_flat_env_vars(cls, values: object) -> object:
        """Support flat env vars for local development ergonomics."""
        if not isinstance(values, dict):
            return values

        mapped = dict(values)
        bot = dict(mapped.get("bot", {}))
        db = dict(mapped.get("db", {}))
        app = dict(mapped.get("app", {}))

        if "BOT_TOKEN" in mapped and "token" not in bot:
            bot["token"] = mapped["BOT_TOKEN"]
        if "DATABASE_URL" in mapped and "dsn" not in db:
            db["dsn"] = mapped["DATABASE_URL"]
        if "APP_ENV" in mapped and "env" not in app:
            app["env"] = mapped["APP_ENV"]
        if "DEBUG" in mapped and "debug" not in app:
            app["debug"] = mapped["DEBUG"]

        if bot:
            mapped["bot"] = bot
        if db:
            mapped["db"] = db
        if app:
            mapped["app"] = app

        return mapped


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache settings."""
    return Settings()
