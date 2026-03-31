from typing import cast

from app.backends import (
    HelperAdapterStub,
    HelperCommand,
    HelperCommandRequest,
    HelperErrorCode,
)
from app.backends.helper_protocol import ReadOnlyHelperCommand


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


def test_adapter_unsupported_command_returns_error_result() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest(
        command=cast(ReadOnlyHelperCommand, HelperCommand.PEER_ADD),
        payload={},
    )

    result = adapter.execute(request)

    assert result.success is False
    assert result.error is not None
    assert result.error.code is HelperErrorCode.UNKNOWN_COMMAND


def test_request_to_adapter_to_result_roundtrip_shape() -> None:
    adapter = HelperAdapterStub()
    request = HelperCommandRequest.from_dict(
        {"command": HelperCommand.HEALTHCHECK.value, "payload": {}},
    )

    result = adapter.execute(request)

    assert result.to_dict() == {
        "success": True,
        "payload": {"ok": True, "detail": "stub-adapter"},
        "error": None,
    }
