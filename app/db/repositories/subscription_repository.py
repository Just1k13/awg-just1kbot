"""Repository helpers for subscriptions."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Subscription


class SubscriptionRepository:
    """Minimal subscription repository."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_latest_for_user(self, user_id: int) -> Subscription | None:
        stmt = (
            select(Subscription)
            .where(Subscription.user_id == user_id)
            .order_by(Subscription.id.desc())
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()
