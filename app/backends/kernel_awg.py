"""Linux kernel AWG backend stub.

This module intentionally exposes only a contract-compliant stub for the future
integration with `amneziawg-linux-kernel-module` and `amneziawg-tools`.
The project is currently in foundation phase, so backend runtime operations are
not implemented yet.
"""

from app.backends.base import (
    AwgBackend,
    CreatePeerInput,
    CreatePeerResult,
    PeerRuntimeState,
    RenderProfileConfigResult,
)
from app.db.models import Node, ProfileNode


class KernelAwgBackend(AwgBackend):
    """Stub implementation for single-node Linux kernel AWG backend."""

    async def healthcheck(self, node: Node) -> bool:
        """Check whether node-level AWG runtime is healthy."""
        # TODO: run helper-mediated health probe (awg/tooling availability).
        # TODO: wire to node-helper contract so bot process does not require root.
        raise NotImplementedError("Kernel AWG healthcheck is not implemented yet")

    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Render exported client config for a profile-node mapping."""
        # TODO: render client config from stored peer/node metadata.
        # TODO: keep config rendering behind node-helper/api boundary.
        raise NotImplementedError("Kernel AWG config render is not implemented yet")

    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Create a peer in kernel AWG runtime."""
        # TODO: call awg peer-add via node-helper when helper contract is ready.
        raise NotImplementedError("Kernel AWG peer creation is not implemented yet")

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable an existing peer without deleting profile metadata."""
        # TODO: call awg peer-disable via node-helper.
        raise NotImplementedError("Kernel AWG peer disable is not implemented yet")

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete peer from kernel AWG runtime."""
        # TODO: call awg peer-delete via node-helper.
        raise NotImplementedError("Kernel AWG peer delete is not implemented yet")

    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeState:
        """Read current peer runtime state from kernel AWG runtime."""
        # TODO: read runtime state from awg peer-show/peer-list via node-helper.
        raise NotImplementedError("Kernel AWG peer runtime read is not implemented yet")
