"""Linux kernel AWG backend stub.

This module intentionally exposes only a contract-compliant stub for the future
integration with `amneziawg-linux-kernel-module` and `amneziawg-tools`.
The project is currently in foundation phase, so backend runtime operations are
not implemented yet.
"""

from app.backends.base import (
    AwgBackend,
    BackendCapabilitySnapshot,
    CreatePeerInput,
    CreatePeerResult,
    HealthcheckResult,
    PeerRuntimeState,
    RenderProfileConfigResult,
)
from app.backends.helper_contract import HelperCommand
from app.db.models import Node, ProfileNode


class KernelAwgBackend(AwgBackend):
    """Stub implementation for single-node Linux kernel AWG backend."""

    async def healthcheck(self, node: Node) -> HealthcheckResult:
        """Check whether node-level AWG runtime is healthy."""
        # TODO: run helper-mediated health probe (no direct root-required calls in bot process).
        # TODO: wire healthcheck to node-helper command: `healthcheck`.
        raise NotImplementedError("Kernel AWG healthcheck is not implemented yet")

    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Render exported client config for a profile-node mapping."""
        # TODO: render client config from stored peer/node metadata.
        # TODO: wire to node-helper command: `config-render`.
        raise NotImplementedError("Kernel AWG config render is not implemented yet")

    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Create a peer in kernel AWG runtime."""
        # TODO: call node-helper `peer-add`.
        raise NotImplementedError("Kernel AWG peer creation is not implemented yet")

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable an existing peer without deleting profile metadata."""
        # TODO: call node-helper `peer-disable`.
        raise NotImplementedError("Kernel AWG peer disable is not implemented yet")

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete peer from kernel AWG runtime."""
        # TODO: call node-helper `peer-delete`.
        raise NotImplementedError("Kernel AWG peer delete is not implemented yet")

    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeState:
        """Read current peer runtime state from kernel AWG runtime."""
        # TODO: read runtime state via node-helper `peer-show` / `peer-list`.
        raise NotImplementedError("Kernel AWG peer runtime read is not implemented yet")

    async def list_peer_runtime(self, node: Node) -> tuple[PeerRuntimeState, ...]:
        """List runtime state for peers from kernel AWG runtime."""
        # TODO: read peer list via node-helper `peer-list`.
        raise NotImplementedError("Kernel AWG peer runtime list is not implemented yet")

    def get_capabilities(self) -> BackendCapabilitySnapshot:
        """Describe capability surface of the kernel backend stub."""
        return BackendCapabilitySnapshot(
            backend_name="kernel_awg",
            helper_commands=frozenset(HelperCommand),
            supports_runtime_inspection=True,
            supports_config_rendering=True,
            supports_peer_mutation=False,
        )
