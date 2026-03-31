from app.backends import HelperCommand, HelperCommandRequest, StubHelperClient


def test_stub_helper_client_smoke() -> None:
    client = StubHelperClient()

    result = client.execute(HelperCommandRequest(command=HelperCommand.HEALTHCHECK, payload={}))

    assert result.success is True
    assert result.payload == {"ok": True, "detail": "stub-adapter"}


def test_stub_helper_client_request_result_roundtrip() -> None:
    client = StubHelperClient()
    request = HelperCommandRequest.from_dict(
        {"command": HelperCommand.PEER_SHOW.value, "payload": {"public_key": "pk-1"}},
    )

    result = client.execute(request)

    assert result.to_dict() == {
        "success": True,
        "payload": {
            "enabled": False,
            "public_key": "pk-1",
            "endpoint": None,
            "last_handshake_at": None,
            "rx_bytes": 0,
            "tx_bytes": 0,
        },
        "error": None,
    }


def test_stub_helper_client_mutation_path_roundtrip() -> None:
    client = StubHelperClient()
    request = HelperCommandRequest.from_dict(
        {
            "command": HelperCommand.PEER_ADD.value,
            "payload": {"profile_node_id": 42, "node_id": 1, "profile_id": 9},
        },
    )

    result = client.execute(request)

    assert result.to_dict() == {
        "success": True,
        "payload": {"backend_peer_id": "stub-peer-42"},
        "error": None,
    }
