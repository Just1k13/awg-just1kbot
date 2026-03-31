"""Minimal backend contract for future AWG runtime integration."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from app.db.models import Node, ProfileNode


@dataclass(slots=True, frozen=True)
class CreatePeerInput:
    """Input data required to create a backend peer for a profile-node mapping."""

    profile_node: ProfileNode


@dataclass(slots=True, frozen=True)
class CreatePeerResult:
    """Result of successful peer creation in a backend runtime."""

    backend_peer_id: str


@dataclass(slots=True, frozen=True)
class RenderProfileConfigResult:
    """Rendered client configuration payload prepared for profile export."""

    content: str
    file_name: str = "client.conf"


@dataclass(slots=True, frozen=True)
class PeerRuntimeState:
    """Observed peer runtime state from backend."""

    enabled: bool
    last_handshake_at: datetime | None = None
    rx_bytes: int | None = None
    tx_bytes: int | None = None
    endpoint: str | None = None


class AwgBackend(ABC):
    """Minimal contract for the AWG backend layer."""

    @abstractmethod
    async def healthcheck(self, node: Node) -> bool:
        """Validate that a node is reachable and backend-ready."""

    @abstractmethod
    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Render client config payload for a profile-node mapping."""

    @abstractmethod
    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Create a peer in backend runtime."""

    @abstractmethod
    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable a peer in backend runtime without deleting metadata."""

    @abstractmethod
    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete a peer from backend runtime permanently."""

    @abstractmethod
    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeState:
        """Return current peer runtime status from backend."""
