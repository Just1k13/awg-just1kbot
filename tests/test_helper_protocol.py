import pytest

from app.backends import (
    READ_ONLY_HELPER_COMMANDS,
    ConfigRenderResponse,
    HealthcheckResponse,
    HelperCommand,
    HelperCommandRequest,
    HelperCommandResult,
    HelperErrorCode,
    HelperProtocolError,
    PeerListItem,
    PeerListResponse,
    PeerShowResponse,
)


def test_helper_request_roundtrip_read_only_command() -> None:
    request = HelperCommandRequest(
        command=HelperCommand.HEALTHCHECK,
        payload={"node_slug": "default"},
    )

    restored = HelperCommandRequest.from_dict(request.to_dict())

    assert restored == request


def test_helper_request_rejects_mutation_command() -> None:
    with pytest.raises(ValueError, match="not read-only"):
        HelperCommandRequest.from_dict(
            {"command": HelperCommand.PEER_ADD.value, "payload": {"peer_id": "peer-1"}},
        )


def test_helper_result_envelope_validation_and_serialization() -> None:
    success = HelperCommandResult(success=True, payload={"ok": True})
    failure = HelperCommandResult(
        success=False,
        error=HelperProtocolError(
            code=HelperErrorCode.HELPER_UNAVAILABLE,
            message="helper process is not running",
        ),
    )

    assert success.to_dict() == {"success": True, "payload": {"ok": True}, "error": None}
    assert failure.to_dict() == {
        "success": False,
        "payload": None,
        "error": {
            "code": HelperErrorCode.HELPER_UNAVAILABLE.value,
            "message": "helper process is not running",
        },
    }


def test_read_only_protocol_payload_dto_smoke() -> None:
    health = HealthcheckResponse(ok=True)
    peer_show = PeerShowResponse(enabled=False, public_key="abc")
    peer_list = PeerListResponse(peers=(PeerListItem(public_key="abc", enabled=False),))
    rendered = ConfigRenderResponse(content="[Interface]")

    assert health.ok is True
    assert peer_show.endpoint is None
    assert peer_list.peers[0].public_key == "abc"
    assert rendered.file_name == "client.conf"


def test_read_only_commands_constant_matches_expected_subset() -> None:
    assert set(READ_ONLY_HELPER_COMMANDS) == {
        HelperCommand.HEALTHCHECK,
        HelperCommand.PEER_SHOW,
        HelperCommand.PEER_LIST,
        HelperCommand.CONFIG_RENDER,
    }
