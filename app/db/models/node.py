"""Node model."""

from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Node(Base):
    """Single-node AWG runtime definition."""

    __tablename__ = "nodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    public_host: Mapped[str] = mapped_column(String(255))
    public_port: Mapped[int] = mapped_column(Integer)
    interface_name: Mapped[str] = mapped_column(String(64))
    subnet_cidr: Mapped[str] = mapped_column(String(64))
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
