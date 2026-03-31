import asyncio
from typing import cast

import pytest

from app.backends import (
    AwgBackend,
    CreatePeerInput,
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

    assert rendered.file_name == "client.conf"
    assert runtime.last_handshake_at is None


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
