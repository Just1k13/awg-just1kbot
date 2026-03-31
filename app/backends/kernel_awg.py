"""Single-node Linux kernel AWG backend stub.

This module defines the boundary for future helper-mediated integration with
`amneziawg-linux-kernel-module` and `amneziawg-tools`.

Read-only methods map to future helper commands:
- `healthcheck` -> `healthcheck`
- `get_peer_runtime` -> `peer-show`
- `list_peer_runtime` -> `peer-list`
- `render_profile_config` -> `config-render`

Mutation methods stay unimplemented in this phase:
- `create_peer`, `disable_peer`, `delete_peer`
"""

from app.backends.base import (
    AwgBackend,
    CreatePeerInput,
    CreatePeerResult,
    NodeHealthSnapshot,
    PeerRuntimeSnapshot,
    RenderProfileConfigResult,
)
from app.db.models import Node, ProfileNode


class KernelAwgBackend(AwgBackend):
    """Stub implementation for single-node Linux kernel AWG backend."""

    async def healthcheck(self, node: Node) -> NodeHealthSnapshot:
        """Read-only node health snapshot (future helper `healthcheck`)."""
        # TODO: wire to node-helper `healthcheck`.
        raise NotImplementedError("Kernel AWG healthcheck is not implemented yet")

    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeSnapshot:
        """Read-only runtime snapshot for one peer (future helper `peer-show`)."""
        # TODO: wire to node-helper `peer-show`.
        raise NotImplementedError("Kernel AWG peer runtime read is not implemented yet")

    async def list_peer_runtime(self, node: Node) -> tuple[PeerRuntimeSnapshot, ...]:
        """Read-only runtime snapshots for all peers (future helper `peer-list`)."""
        # TODO: wire to node-helper `peer-list`.
        raise NotImplementedError("Kernel AWG peer runtime list is not implemented yet")

    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Read-only client config export path (future helper `config-render`)."""
        # TODO: wire to node-helper `config-render`.
        raise NotImplementedError("Kernel AWG config render is not implemented yet")

    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Future mutation method (`peer-add`), intentionally not implemented."""
        # TODO: call node-helper `peer-add`.
        raise NotImplementedError("Kernel AWG peer creation is not implemented yet")

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Future mutation method (`peer-disable`), intentionally not implemented."""
        # TODO: call node-helper `peer-disable`.
        raise NotImplementedError("Kernel AWG peer disable is not implemented yet")

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Future mutation method (`peer-delete`), intentionally not implemented."""
        # TODO: call node-helper `peer-delete`.
        raise NotImplementedError("Kernel AWG peer delete is not implemented yet")
