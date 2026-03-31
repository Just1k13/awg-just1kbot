"""Linux kernel AWG backend stub.

This module intentionally exposes only a contract-compliant stub for the future
integration with `amneziawg-linux-kernel-module` and `amneziawg-tools`.
The project is currently in foundation phase, so backend runtime operations are
not implemented yet.
"""

from __future__ import annotations

from datetime import datetime

from app.backends.base import (
    AwgBackend,
    BackendCapabilitySnapshot,
    CreatePeerInput,
    CreatePeerResult,
    HealthcheckResult,
    PeerRuntimeState,
    RenderProfileConfigResult,
)
from app.backends.helper_client import HelperClient, StubHelperClient
from app.backends.helper_contract import HelperCommand
from app.backends.helper_protocol import HelperCommandRequest, HelperCommandResult
from app.db.models import Node, ProfileNode


class KernelAwgBackendError(RuntimeError):
    """Backend-level error raised when helper-facing read-only call fails."""


class KernelAwgBackend(AwgBackend):
    """Stub implementation for single-node Linux kernel AWG backend."""

    def __init__(self, helper_client: HelperClient | None = None) -> None:
        self._helper_client = helper_client or StubHelperClient()

    async def healthcheck(self, node: Node) -> HealthcheckResult:
        """Check whether node-level AWG runtime is healthy."""
        result = self._execute_read_only_command(
            command=HelperCommand.HEALTHCHECK,
            payload={"node_id": node.id, "node_code": node.code},
        )
        payload = result.payload or {}
        return HealthcheckResult(
            ok=bool(payload.get("ok", False)),
            detail=self._optional_string(payload.get("detail")),
        )

    async def render_profile_config(
        self,
        profile_node: ProfileNode,
    ) -> RenderProfileConfigResult:
        """Render exported client config for a profile-node mapping."""
        result = self._execute_read_only_command(
            command=HelperCommand.CONFIG_RENDER,
            payload={
                "profile_node_id": profile_node.id,
                "node_id": profile_node.node_id,
                "profile_id": profile_node.profile_id,
            },
        )
        payload = result.payload or {}
        content = payload.get("content")
        if not isinstance(content, str):
            raise KernelAwgBackendError("helper config-render payload must include string content")
        file_name = payload.get("file_name")
        if not isinstance(file_name, str):
            file_name = "client.conf"
        return RenderProfileConfigResult(content=content, file_name=file_name)

    async def create_peer(self, request: CreatePeerInput) -> CreatePeerResult:
        """Create a peer in kernel AWG runtime."""
        # TODO: call node-helper `peer-add`.
        raise NotImplementedError("Kernel AWG peer creation is not implemented yet")

    async def disable_peer(self, profile_node: ProfileNode) -> None:
        """Disable an existing peer without deleting profile metadata."""
        # TODO: call node-helper `peer-disable`.
        raise NotImplementedError("Kernel AWG peer disable is not implemented yet")

    async def delete_peer(self, profile_node: ProfileNode) -> None:
        """Delete peer from kernel AWG runtime."""
        # TODO: call node-helper `peer-delete`.
        raise NotImplementedError("Kernel AWG peer delete is not implemented yet")

    async def get_peer_runtime(self, profile_node: ProfileNode) -> PeerRuntimeState:
        """Read current peer runtime state from kernel AWG runtime."""
        result = self._execute_read_only_command(
            command=HelperCommand.PEER_SHOW,
            payload={
                "profile_node_id": profile_node.id,
                "node_id": profile_node.node_id,
                "profile_id": profile_node.profile_id,
                "public_key": profile_node.backend_peer_id,
            },
        )
        return self._peer_runtime_from_payload(result.payload or {})

    async def list_peer_runtime(self, node: Node) -> tuple[PeerRuntimeState, ...]:
        """List runtime state for peers from kernel AWG runtime."""
        result = self._execute_read_only_command(
            command=HelperCommand.PEER_LIST,
            payload={"node_id": node.id, "node_code": node.code},
        )
        payload = result.payload or {}
        peers = payload.get("peers")
        if not isinstance(peers, (list, tuple)):
            raise KernelAwgBackendError("helper peer-list payload must include a peers list")

        states: list[PeerRuntimeState] = []
        for peer in peers:
            if not isinstance(peer, dict):
                raise KernelAwgBackendError("helper peer-list item must be a mapping")
            states.append(
                PeerRuntimeState(
                    enabled=bool(peer.get("enabled", False)),
                    endpoint=self._optional_string(peer.get("endpoint")),
                    last_handshake_at=self._parse_optional_datetime(peer.get("last_handshake_at")),
                    rx_bytes=self._optional_int(peer.get("rx_bytes")),
                    tx_bytes=self._optional_int(peer.get("tx_bytes")),
                )
            )
        return tuple(states)

    def get_capabilities(self) -> BackendCapabilitySnapshot:
        """Describe capability surface of the kernel backend stub."""
        return BackendCapabilitySnapshot(
            backend_name="kernel_awg",
            helper_commands=frozenset(HelperCommand),
            supports_runtime_inspection=True,
            supports_config_rendering=True,
            supports_peer_mutation=False,
        )

    def _execute_read_only_command(
        self,
        command: HelperCommand,
        payload: dict[str, object],
    ) -> HelperCommandResult:
        result = self._helper_client.execute(
            HelperCommandRequest(command=command, payload=payload),
        )
        if result.success:
            return result

        if result.error is None:
            raise KernelAwgBackendError(
                f"helper command {command.value!r} failed without protocol error",
            )
        raise KernelAwgBackendError(
            f"helper command {command.value!r} failed: "
            f"{result.error.code.value}: {result.error.message}",
        )

    def _peer_runtime_from_payload(self, payload: dict[str, object]) -> PeerRuntimeState:
        return PeerRuntimeState(
            enabled=bool(payload.get("enabled", False)),
            endpoint=self._optional_string(payload.get("endpoint")),
            last_handshake_at=self._parse_optional_datetime(payload.get("last_handshake_at")),
            rx_bytes=self._optional_int(payload.get("rx_bytes")),
            tx_bytes=self._optional_int(payload.get("tx_bytes")),
        )

    @staticmethod
    def _optional_string(value: object) -> str | None:
        return value if isinstance(value, str) else None

    @staticmethod
    def _optional_int(value: object) -> int | None:
        return value if isinstance(value, int) else None

    @staticmethod
    def _parse_optional_datetime(value: object) -> datetime | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise KernelAwgBackendError("helper datetime field must be a string or null")
        try:
            return datetime.fromisoformat(value)
        except ValueError as exc:
            raise KernelAwgBackendError(f"invalid helper datetime value: {value!r}") from exc
