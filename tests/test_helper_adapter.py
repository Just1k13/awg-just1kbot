from app.backends import HelperAdapterStub, HelperCommand, HelperCommandRequest


def test_adapter_healthcheck_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(command=HelperCommand.HEALTHCHECK, payload={})

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {"ok": True, "detail": "stub-adapter"}


def test_adapter_peer_show_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=HelperCommand.PEER_SHOW,
        payload={"public_key": "peer-test-key"},
    )

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {
        "enabled": False,
        "public_key": "peer-test-key",
        "endpoint": None,
        "last_handshake_at": None,
        "rx_bytes": 0,
        "tx_bytes": 0,
    }


def test_adapter_peer_list_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(command=HelperCommand.PEER_LIST, payload={})

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {"peers": ()}


def test_adapter_config_render_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(command=HelperCommand.CONFIG_RENDER, payload={})

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {
        "content": "# helper adapter stub\n[Interface]\n# TODO: wire real helper",
        "file_name": "client.conf",
    }


def test_adapter_peer_add_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=HelperCommand.PEER_ADD,
        payload={"profile_node_id": 5, "node_id": 1, "profile_id": 11},
    )

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {"backend_peer_id": "stub-peer-5"}


def test_adapter_peer_disable_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=HelperCommand.PEER_DISABLE,
        payload={
            "profile_node_id": 5,
            "node_id": 1,
            "profile_id": 11,
            "backend_peer_id": "peer-5",
        },
    )

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {}


def test_adapter_peer_delete_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=HelperCommand.PEER_DELETE,
        payload={
            "profile_node_id": 5,
            "node_id": 1,
            "profile_id": 11,
            "backend_peer_id": "peer-5",
        },
    )

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {}


def test_adapter_reconcile_stub_response() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=HelperCommand.RECONCILE,
        payload={"node_id": 1, "node_code": "main"},
    )

    result = adapter.execute(request)

    assert result.success is True
    assert result.payload == {"scanned_peers": 0, "updated_peers": 0, "removed_peers": 0}
