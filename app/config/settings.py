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
    default_node_code: str | None = None


class Settings(BaseSettings):
    """Top-level settings container."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_prefix="",
        extra="ignore",
    )

    bot: BotSettings | None = None
    db: DatabaseSettings | None = None
    app: AppRuntimeSettings = AppRuntimeSettings()

    bot_token: SecretStr | None = Field(default=None, alias="BOT_TOKEN")
    database_url: str | None = Field(default=None, alias="DATABASE_URL")
    app_env: str | None = Field(default=None, alias="APP_ENV")
    debug: bool | None = Field(default=None, alias="DEBUG")
    default_node_code: str | None = Field(default=None, alias="DEFAULT_NODE_CODE")

    @model_validator(mode="after")
    def normalize_flat_env_vars(self) -> "Settings":
        """Support flat env vars for local development ergonomics."""
        if self.bot is None and self.bot_token is not None:
            self.bot = BotSettings(token=self.bot_token)
        if self.db is None and self.database_url is not None:
            self.db = DatabaseSettings(dsn=self.database_url)

        if self.app_env is not None:
            self.app.env = self.app_env
        if self.debug is not None:
            self.app.debug = self.debug
        if self.default_node_code is not None:
            self.app.default_node_code = self.default_node_code

        if self.bot is None or self.db is None:
            raise ValueError("Bot token and database DSN must be configured")

        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache settings."""
    return Settings()
