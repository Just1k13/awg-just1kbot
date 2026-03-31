"""Backend abstraction for AWG integration."""

from abc import ABC, abstractmethod

from app.db.models import Node, ProfileNode


class AwgBackend(ABC):
    """Interface for AWG-related backend operations."""

    @abstractmethod
    async def healthcheck(self, node: Node) -> bool:
        """Validate that a node is reachable and backend-ready."""

    @abstractmethod
    async def render_profile_config(self, profile_node: ProfileNode) -> str:
        """Render configuration payload for a profile-node mapping."""

    @abstractmethod
    async def create_peer(self, profile_node: ProfileNode) -> str:
        """Create a peer and return backend peer identifier."""

    @abstractmethod
    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable a peer in backend without deleting metadata."""

    @abstractmethod
    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete a peer in backend permanently."""
