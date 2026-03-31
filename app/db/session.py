"""Async SQLAlchemy engine and session factory."""

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.config.settings import Settings


def create_engine(settings: Settings) -> AsyncEngine:
    """Create an async SQLAlchemy engine from settings."""
    return create_async_engine(settings.db.dsn, echo=settings.db.echo)


def create_session_factory(settings: Settings) -> async_sessionmaker[AsyncSession]:
    """Create async session factory from settings."""
    engine = create_engine(settings)
    return async_sessionmaker(bind=engine, expire_on_commit=False)
