"""Application-level runtime inspection wiring.

This module orchestrates backend read-only methods only.
It does not execute OS commands and does not mutate runtime state.
"""

from dataclasses import dataclass

from app.backends import (
    AwgBackend,
    BackendCapabilitySnapshot,
    NodeHealthSnapshot,
    PeerRuntimeSnapshot,
)
from app.db.models import Node, ProfileNode


@dataclass(slots=True, frozen=True)
class NodeRuntimeInspection:
    """Aggregated read-only runtime inspection snapshot for a node."""

    health: NodeHealthSnapshot
    peers: tuple[PeerRuntimeSnapshot, ...]


async def inspect_node_runtime(node: Node, backend: AwgBackend) -> NodeRuntimeInspection:
    """Inspect node runtime using backend read-only methods."""
    health = await backend.healthcheck(node)
    peers = await backend.list_peer_runtime(node)
    return NodeRuntimeInspection(health=health, peers=peers)


async def inspect_profile_runtime(
    profile_node: ProfileNode,
    backend: AwgBackend,
) -> PeerRuntimeSnapshot:
    """Inspect a single profile-node runtime snapshot."""
    return await backend.get_peer_runtime(profile_node)


def describe_backend_capabilities(backend: AwgBackend) -> BackendCapabilitySnapshot:
    """Expose static backend capability snapshot for planning-level wiring."""
    get_capabilities = getattr(backend, "get_capabilities", None)
    if callable(get_capabilities):
        return get_capabilities()

    helper_commands = getattr(backend, "helper_commands", ())
    return BackendCapabilitySnapshot(
        backend_name=backend.__class__.__name__,
        helper_commands=frozenset(helper_commands),
        supports_runtime_inspection=False,
        supports_config_rendering=False,
        supports_peer_mutation=False,
    )
