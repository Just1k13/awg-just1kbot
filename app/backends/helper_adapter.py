"""Deterministic helper adapter for read-only protocol commands.

This module intentionally keeps command handling deterministic and in-process.
Helper boundary concerns live in ``app.backends.helper_client``.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import asdict

from app.backends.helper_contract import HelperCommand
from app.backends.helper_protocol import (
    ConfigRenderResponse,
    HealthcheckResponse,
    HelperCommandRequest,
    HelperCommandResult,
    HelperErrorCode,
    HelperProtocolError,
    PeerListResponse,
    PeerShowResponse,
)


class HelperAdapterStub:
    """In-process stub adapter for helper protocol requests.

    TODO: Replace this deterministic stub with real helper boundary wiring.
    """

    def execute(self, request: HelperCommandRequest) -> HelperCommandResult:
        """Return deterministic read-only results without runtime/system calls."""
        handlers: dict[HelperCommand, Callable[[dict[str, object]], HelperCommandResult]] = {
            HelperCommand.HEALTHCHECK: self._handle_healthcheck,
            HelperCommand.PEER_SHOW: self._handle_peer_show,
            HelperCommand.PEER_LIST: self._handle_peer_list,
            HelperCommand.CONFIG_RENDER: self._handle_config_render,
        }

        handler = handlers.get(request.command)
        if handler is None:
            return HelperCommandResult(
                success=False,
                error=HelperProtocolError(
                    code=HelperErrorCode.UNKNOWN_COMMAND,
                    message=f"unsupported command: {request.command.value}",
                ),
            )

        return handler(request.payload)

    def _handle_healthcheck(self, _payload: dict[str, object]) -> HelperCommandResult:
        response = HealthcheckResponse(ok=True, detail="stub-adapter")
        return HelperCommandResult(success=True, payload=asdict(response))

    def _handle_peer_show(self, payload: dict[str, object]) -> HelperCommandResult:
        peer_public_key = payload.get("public_key")
        if not isinstance(peer_public_key, str):
            peer_public_key = "stub-peer-public-key"

        response = PeerShowResponse(
            enabled=False,
            public_key=peer_public_key,
            endpoint=None,
            last_handshake_at=None,
            rx_bytes=0,
            tx_bytes=0,
        )
        return HelperCommandResult(success=True, payload=asdict(response))

    def _handle_peer_list(self, _payload: dict[str, object]) -> HelperCommandResult:
        response = PeerListResponse(peers=())
        return HelperCommandResult(success=True, payload=asdict(response))

    def _handle_config_render(self, _payload: dict[str, object]) -> HelperCommandResult:
        response = ConfigRenderResponse(
            content="# helper adapter stub\n[Interface]\n# TODO: wire real helper",
        )
        return HelperCommandResult(success=True, payload=asdict(response))
