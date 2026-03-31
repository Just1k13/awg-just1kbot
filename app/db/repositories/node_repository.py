"""Repository helpers for nodes."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Node


class NodeRepository:
    """Minimal node repository."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_active(self) -> list[Node]:
        stmt = select(Node).where(Node.is_active.is_(True)).order_by(Node.id)
        result = await self._session.execute(stmt)
        return list(result.scalars().all())
