"""Protocol draft DTOs for future read-only node-helper interaction."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any, Literal

from app.backends.helper_contract import READ_ONLY_HELPER_COMMANDS, HelperCommand


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


@dataclass(slots=True, frozen=True)
class HelperCommandRequest:
    """Generic request envelope for read-only helper commands."""

    command: ReadOnlyHelperCommand
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-safe mapping."""
        return {"command": self.command.value, "payload": self.payload}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HelperCommandRequest:
        """Build a request envelope from plain mapping data."""
        command = HelperCommand(data["command"])
        cls._ensure_read_only_command(command)

        payload = data.get("payload")
        if not isinstance(payload, dict):
            raise ValueError("payload must be a dictionary")

        return cls(command=command, payload=payload)

    @staticmethod
    def _ensure_read_only_command(command: HelperCommand) -> None:
        if command not in READ_ONLY_HELPER_COMMANDS:
            raise ValueError(f"command {command.value!r} is not read-only")


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
