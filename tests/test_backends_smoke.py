import asyncio
from typing import cast

import pytest

from app.backends import (
    AwgBackend,
    BackendCapabilitySnapshot,
    CreatePeerInput,
    HealthcheckResult,
    HelperCommand,
    KernelAwgBackend,
    PeerRuntimeState,
    RenderProfileConfigResult,
)
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


def test_kernel_awg_stub_methods_raise_not_implemented() -> None:
    backend = KernelAwgBackend()
    profile_node = cast(ProfileNode, object())
    node = cast(Node, object())

    with pytest.raises(NotImplementedError):
        asyncio.run(backend.healthcheck(node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.render_profile_config(profile_node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.create_peer(CreatePeerInput(profile_node=profile_node)))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.disable_peer(profile_node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.delete_peer(profile_node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.get_peer_runtime(profile_node))
    with pytest.raises(NotImplementedError):
        asyncio.run(backend.list_peer_runtime(node))


def test_kernel_awg_capabilities_smoke() -> None:
    capabilities = KernelAwgBackend().get_capabilities()

    assert isinstance(capabilities, BackendCapabilitySnapshot)
    assert capabilities.backend_name == "kernel_awg"
    assert capabilities.supports_runtime_inspection is True
