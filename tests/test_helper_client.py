from typing import cast

from app.backends import (
    HelperAdapterStub,
    HelperCommand,
    HelperCommandRequest,
    HelperErrorCode,
    StubHelperClient,
)
from app.backends.helper_protocol import ReadOnlyHelperCommand


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


def test_stub_helper_client_uses_adapter_for_unknown_command() -> None:
    client = StubHelperClient(adapter=HelperAdapterStub())
    request = HelperCommandRequest(
        command=cast(ReadOnlyHelperCommand, HelperCommand.PEER_ADD),
        payload={},
    )

    result = client.execute(request)

    assert result.success is False
    assert result.error is not None
    assert result.error.code is HelperErrorCode.UNKNOWN_COMMAND
