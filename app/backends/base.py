"""Minimal backend contract for future AWG runtime integration."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from app.backends.helper_contract import (
    MUTATION_HELPER_COMMANDS,
    READ_ONLY_HELPER_COMMANDS,
    HelperCommand,
)
from app.db.models import Node, ProfileNode


@dataclass(slots=True, frozen=True)
class NodeHealthSnapshot:
    """Read-only node health snapshot."""

    ok: bool
    detail: str | None = None
    checked_at: datetime | None = None


@dataclass(slots=True, frozen=True)
class PeerRuntimeSnapshot:
    """Read-only peer runtime snapshot."""

    enabled: bool
    last_handshake_at: datetime | None = None
    rx_bytes: int | None = None
    tx_bytes: int | None = None
    endpoint: str | None = None


@dataclass(slots=True, frozen=True)
class BackendCapabilitySnapshot:
    """Backend capabilities snapshot for planning/wiring decisions."""

    read_only_commands: tuple[HelperCommand, ...]
    mutation_commands: tuple[HelperCommand, ...]


@dataclass(slots=True, frozen=True)
class ConfigRenderMetadata:
    """Metadata for rendered client config export."""

    file_name: str = "client.conf"
    content_type: str = "text/plain"


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
    metadata: ConfigRenderMetadata = ConfigRenderMetadata()


class AwgBackend(ABC):
    """Minimal contract for the AWG backend layer."""

    @property
    def supported_helper_commands(self) -> tuple[HelperCommand, ...]:
        """Commands this backend expects from the future node-helper boundary."""
        return (
            *self.read_only_helper_commands,
            *self.mutation_helper_commands,
        )

    @property
    def read_only_helper_commands(self) -> tuple[HelperCommand, ...]:
        """Read-only helper commands used for runtime inspection."""
        return READ_ONLY_HELPER_COMMANDS

    @property
    def mutation_helper_commands(self) -> tuple[HelperCommand, ...]:
        """Mutation helper commands reserved for future implementation."""
        return MUTATION_HELPER_COMMANDS

    def get_capabilities(self) -> BackendCapabilitySnapshot:
        """Return static capability snapshot for application-level planning."""
        return BackendCapabilitySnapshot(
            read_only_commands=self.read_only_helper_commands,
            mutation_commands=self.mutation_helper_commands,
        )

    # Read-only runtime inspection
    @abstractmethod
    async def healthcheck(self, node: Node) -> NodeHealthSnapshot:
        """Validate that a node is reachable and backend-ready."""

    @abstractmethod
    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeSnapshot:
        """Return current runtime status for a specific peer mapping."""

    @abstractmethod
    async def list_peer_runtime(self, node: Node) -> tuple[PeerRuntimeSnapshot, ...]:
        """Return read-only runtime snapshots for all peers on a node."""

    @abstractmethod
    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Render client config payload for a profile-node mapping."""

    # Future mutation methods
    @abstractmethod
    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Create a peer in backend runtime."""

    @abstractmethod
    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable a peer in backend runtime without deleting metadata."""

    @abstractmethod
    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete a peer from backend runtime permanently."""
