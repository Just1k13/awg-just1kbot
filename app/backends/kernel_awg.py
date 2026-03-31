"""Kernel AWG backend stub.

This module intentionally contains only interface-compliant stubs.
Real backend logic will be added incrementally in future phases.
"""

from app.backends.base import AwgBackend
from app.db.models import Node, ProfileNode


class KernelAwgBackend(AwgBackend):
    """Stub implementation for Linux kernel AWG backend."""

    async def healthcheck(self, node: Node) -> bool:
        """Check backend health for the provided node.

        TODO: add real health probe against the target host.
        """
        raise NotImplementedError("TODO: implement node healthcheck")

    async def render_profile_config(self, profile_node: ProfileNode) -> str:
        """Render config for a profile-node binding.

        TODO: implement profile rendering/export format.
        """
        raise NotImplementedError("TODO: implement profile config rendering")

    async def create_peer(self, profile_node: ProfileNode) -> str:
        """Create peer in AWG backend.

        TODO: implement real peer provisioning.
        """
        raise NotImplementedError("TODO: implement peer creation")

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable peer in AWG backend.

        TODO: implement safe peer disable flow.
        """
        raise NotImplementedError("TODO: implement peer disable")

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete peer in AWG backend.

        TODO: implement peer deletion flow.
        """
        raise NotImplementedError("TODO: implement peer deletion")
