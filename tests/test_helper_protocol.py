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
    PeerAddRequest,
    PeerAddResponse,
    PeerDeleteRequest,
    PeerDisableRequest,
    PeerListItem,
    PeerListResponse,
    PeerShowResponse,
    ReconcileRequest,
    ReconcileResponse,
)


def test_helper_request_roundtrip_read_only_command() -> None:
    request = HelperCommandRequest(
        command=HelperCommand.HEALTHCHECK,
        payload={"node_slug": "default"},
    )

    restored = HelperCommandRequest.from_dict(request.to_dict())

    assert restored == request


def test_helper_request_roundtrip_mutation_command() -> None:
    request = HelperCommandRequest(
        command=HelperCommand.PEER_ADD,
        payload={"profile_node_id": 11, "node_id": 5, "profile_id": 7},
    )

    restored = HelperCommandRequest.from_dict(request.to_dict())

    assert restored == request


def test_helper_request_rejects_non_dict_payload() -> None:
    with pytest.raises(ValueError, match="payload must be a dictionary"):
        HelperCommandRequest.from_dict(
            {"command": HelperCommand.PEER_ADD.value, "payload": "invalid"},
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


def test_protocol_payload_dto_smoke() -> None:
    health = HealthcheckResponse(ok=True)
    peer_show = PeerShowResponse(enabled=False, public_key="abc")
    peer_list = PeerListResponse(peers=(PeerListItem(public_key="abc", enabled=False),))
    rendered = ConfigRenderResponse(content="[Interface]")
    peer_add_req = PeerAddRequest(profile_node_id=1, node_id=2, profile_id=3)
    peer_add_resp = PeerAddResponse(backend_peer_id="stub-peer-1")
    peer_disable_req = PeerDisableRequest(
        profile_node_id=1,
        node_id=2,
        profile_id=3,
        backend_peer_id="peer-1",
    )
    peer_delete_req = PeerDeleteRequest(
        profile_node_id=1,
        node_id=2,
        profile_id=3,
        backend_peer_id="peer-1",
    )
    reconcile_req = ReconcileRequest(node_id=7, node_code="main")
    reconcile_resp = ReconcileResponse(scanned_peers=0, updated_peers=0, removed_peers=0)

    assert health.ok is True
    assert peer_show.endpoint is None
    assert peer_list.peers[0].public_key == "abc"
    assert rendered.file_name == "client.conf"
    assert peer_add_req.profile_node_id == 1
    assert peer_add_resp.backend_peer_id == "stub-peer-1"
    assert peer_disable_req.backend_peer_id == "peer-1"
    assert peer_delete_req.backend_peer_id == "peer-1"
    assert reconcile_req.node_code == "main"
    assert reconcile_resp.updated_peers == 0


def test_read_only_commands_constant_matches_expected_subset() -> None:
    assert set(READ_ONLY_HELPER_COMMANDS) == {
        HelperCommand.HEALTHCHECK,
        HelperCommand.PEER_SHOW,
        HelperCommand.PEER_LIST,
        HelperCommand.CONFIG_RENDER,
    }
