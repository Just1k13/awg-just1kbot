"""Protocol draft DTOs for future node-helper interaction."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any, Literal

from app.backends.helper_contract import HelperCommand


class HelperErrorCode(StrEnum):
    """Minimal error codes for helper protocol envelope."""

    UNKNOWN_COMMAND = "unknown-command"
    INVALID_PAYLOAD = "invalid-payload"
    HELPER_UNAVAILABLE = "helper-unavailable"
    INTERNAL_ERROR = "internal-error"


@dataclass(slots=True, frozen=True)
class HelperProtocolError:
    """Error payload returned by helper-facing protocol draft."""

    code: HelperErrorCode
    message: str

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-safe mapping."""
        data = asdict(self)
        data["code"] = self.code.value
        return data


type ReadOnlyHelperCommand = Literal[
    HelperCommand.HEALTHCHECK,
    HelperCommand.PEER_SHOW,
    HelperCommand.PEER_LIST,
    HelperCommand.CONFIG_RENDER,
]

type MutationHelperCommand = Literal[
    HelperCommand.PEER_ADD,
    HelperCommand.PEER_DISABLE,
    HelperCommand.PEER_DELETE,
    HelperCommand.RECONCILE,
]


@dataclass(slots=True, frozen=True)
class HelperCommandRequest:
    """Generic request envelope for helper commands."""

    command: HelperCommand
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-safe mapping."""
        return {"command": self.command.value, "payload": self.payload}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HelperCommandRequest:
        """Build a request envelope from plain mapping data."""
        command = HelperCommand(data["command"])

        payload = data.get("payload")
        if not isinstance(payload, dict):
            raise ValueError("payload must be a dictionary")

        return cls(command=command, payload=payload)


@dataclass(slots=True, frozen=True)
class HelperCommandResult:
    """Result envelope for helper command execution."""

    success: bool
    payload: dict[str, Any] | None = None
    error: HelperProtocolError | None = None

    def __post_init__(self) -> None:
        if self.success:
            if self.error is not None:
                raise ValueError("successful result cannot include error")
            if self.payload is None:
                object.__setattr__(self, "payload", {})
            return

        if self.error is None:
            raise ValueError("failed result must include error")

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-safe mapping."""
        return {
            "success": self.success,
            "payload": self.payload,
            "error": self.error.to_dict() if self.error else None,
        }


@dataclass(slots=True, frozen=True)
class HealthcheckResponse:
    """Typed payload for healthcheck command."""

    ok: bool
    detail: str | None = None


@dataclass(slots=True, frozen=True)
class PeerShowResponse:
    """Typed payload for peer-show command."""

    enabled: bool
    public_key: str
    endpoint: str | None = None
    last_handshake_at: str | None = None
    rx_bytes: int | None = None
    tx_bytes: int | None = None


@dataclass(slots=True, frozen=True)
class PeerListItem:
    """Single peer entry for peer-list command."""

    public_key: str
    enabled: bool


@dataclass(slots=True, frozen=True)
class PeerListResponse:
    """Typed payload for peer-list command."""

    peers: tuple[PeerListItem, ...]


@dataclass(slots=True, frozen=True)
class ConfigRenderResponse:
    """Typed payload for config-render command."""

    content: str
    file_name: str = "client.conf"


@dataclass(slots=True, frozen=True)
class PeerAddRequest:
    """Typed payload for peer-add command."""

    profile_node_id: int
    node_id: int
    profile_id: int


@dataclass(slots=True, frozen=True)
class PeerAddResponse:
    """Typed payload for successful peer-add command."""

    backend_peer_id: str


@dataclass(slots=True, frozen=True)
class PeerDisableRequest:
    """Typed payload for peer-disable command."""

    profile_node_id: int
    node_id: int
    profile_id: int
    backend_peer_id: str | None


@dataclass(slots=True, frozen=True)
class PeerDeleteRequest:
    """Typed payload for peer-delete command."""

    profile_node_id: int
    node_id: int
    profile_id: int
    backend_peer_id: str | None


@dataclass(slots=True, frozen=True)
class ReconcileRequest:
    """Typed payload for reconcile command."""

    node_id: int
    node_code: str


@dataclass(slots=True, frozen=True)
class ReconcileResponse:
    """Typed payload for deterministic reconcile summary."""

    scanned_peers: int
    updated_peers: int
    removed_peers: int
