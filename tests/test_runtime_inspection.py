import asyncio

from app.backends import (
    AwgBackend,
    BackendCapabilitySnapshot,
    NodeHealthSnapshot,
    PeerRuntimeSnapshot,
)
from app.db.models import Node, ProfileNode
from app.services.runtime_inspection import (
    describe_backend_capabilities,
    inspect_node_runtime,
    inspect_profile_runtime,
)


class DummyBackend(AwgBackend):
    async def healthcheck(self, node: Node) -> NodeHealthSnapshot:
        return NodeHealthSnapshot(ok=True)

    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeSnapshot:
        return PeerRuntimeSnapshot(enabled=True)

    async def list_peer_runtime(self, node: Node) -> tuple[PeerRuntimeSnapshot, ...]:
        return (PeerRuntimeSnapshot(enabled=True),)

    async def render_profile_config(self, profile_node: ProfileNode):
        raise NotImplementedError

    async def create_peer(self, request):
        raise NotImplementedError

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        raise NotImplementedError

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        raise NotImplementedError


def test_inspect_node_runtime_smoke() -> None:
    backend = DummyBackend()
    node = Node(
        code="main",
        public_host="h",
        public_port=1,
        interface_name="i",
        subnet_cidr="s",
        is_active=True,
    )
    result = asyncio.run(inspect_node_runtime(node=node, backend=backend))

    assert result.health.ok is True
    assert len(result.peers) == 1


def test_inspect_profile_runtime_smoke() -> None:
    backend = DummyBackend()
    runtime = asyncio.run(inspect_profile_runtime(profile_node=ProfileNode(), backend=backend))

    assert runtime.enabled is True


def test_describe_backend_capabilities_smoke() -> None:
    capabilities = describe_backend_capabilities(DummyBackend())

    assert isinstance(capabilities, BackendCapabilitySnapshot)
    assert len(capabilities.read_only_commands) > 0
