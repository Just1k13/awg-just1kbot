"""Subscription model."""

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SubscriptionStatus(str, Enum):
    """Subscription lifecycle status."""

    TRIAL = "trial"
    ACTIVE = "active"
    PAUSED = "paused"
    EXPIRED = "expired"


class Subscription(Base):
    """Minimal user subscription record."""

    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    status: Mapped[SubscriptionStatus] = mapped_column(SqlEnum(SubscriptionStatus), index=True)
    plan_code: Mapped[str] = mapped_column(String(50))
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ends_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
