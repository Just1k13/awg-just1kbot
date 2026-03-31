import asyncio
from typing import cast

import pytest

from app.backends import (
    AwgBackend,
    BackendCapabilitySnapshot,
    CreatePeerInput,
    HealthcheckResult,
    HelperCommand,
    HelperCommandResult,
    HelperErrorCode,
    HelperProtocolError,
    KernelAwgBackend,
    KernelAwgBackendError,
    PeerRuntimeState,
    RenderProfileConfigResult,
)
from app.backends.helper_client import HelperClient
from app.db.models import Node, ProfileNode


def test_backend_contract_imports() -> None:
    assert issubclass(KernelAwgBackend, AwgBackend)


def test_backend_dto_smoke() -> None:
    rendered = RenderProfileConfigResult(content="[Interface]")
    runtime = PeerRuntimeState(enabled=False)
    health = HealthcheckResult(ok=True)

    assert rendered.file_name == "client.conf"
    assert runtime.last_handshake_at is None
    assert health.ok is True


def test_helper_command_contract_has_required_commands() -> None:
    required = {
        HelperCommand.PEER_ADD,
        HelperCommand.PEER_DISABLE,
        HelperCommand.PEER_DELETE,
        HelperCommand.PEER_SHOW,
        HelperCommand.PEER_LIST,
        HelperCommand.CONFIG_RENDER,
        HelperCommand.RECONCILE,
        HelperCommand.HEALTHCHECK,
    }
    backend = KernelAwgBackend()
    assert required.issubset(set(backend.supported_helper_commands))


def test_kernel_awg_mutation_methods_raise_not_implemented() -> None:
    backend = KernelAwgBackend()
    profile_node = cast(ProfileNode, object())

    with pytest.raises(NotImplementedError):
        asyncio.run(backend.create_peer(CreatePeerInput(profile_node=profile_node)))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.disable_peer(profile_node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.delete_peer(profile_node))


def test_kernel_awg_read_only_methods_are_wired_to_helper_stub() -> None:
    backend = KernelAwgBackend()
    node = Node(
        code="main",
        public_host="host",
        public_port=51820,
        interface_name="awg0",
        subnet_cidr="10.0.0.0/24",
        is_active=True,
    )
    profile_node = ProfileNode(profile_id=1, node_id=1, backend_peer_id="peer-1", state="active")

    health = asyncio.run(backend.healthcheck(node))
    runtime = asyncio.run(backend.get_peer_runtime(profile_node))
    peers = asyncio.run(backend.list_peer_runtime(node))
    config = asyncio.run(backend.render_profile_config(profile_node))

    assert health.ok is True
    assert health.detail == "stub-adapter"
    assert runtime.enabled is False
    assert runtime.rx_bytes == 0
    assert runtime.tx_bytes == 0
    assert peers == ()
    assert config.file_name == "client.conf"
    assert "# helper adapter stub" in config.content


class FailedHelperClient(HelperClient):
    def execute(self, request):  # type: ignore[no-untyped-def]
        return HelperCommandResult(
            success=False,
            error=HelperProtocolError(
                code=HelperErrorCode.HELPER_UNAVAILABLE,
                message=f"{request.command.value} unavailable",
            ),
        )


def test_kernel_awg_read_only_raises_on_failed_helper_result() -> None:
    backend = KernelAwgBackend(helper_client=FailedHelperClient())
    node = Node(
        code="main",
        public_host="host",
        public_port=51820,
        interface_name="awg0",
        subnet_cidr="10.0.0.0/24",
        is_active=True,
    )

    with pytest.raises(KernelAwgBackendError, match="healthcheck"):
        asyncio.run(backend.healthcheck(node))


def test_kernel_awg_capabilities_smoke() -> None:
    capabilities = KernelAwgBackend().get_capabilities()

    assert isinstance(capabilities, BackendCapabilitySnapshot)
    assert capabilities.backend_name == "kernel_awg"
    assert capabilities.supports_runtime_inspection is True
