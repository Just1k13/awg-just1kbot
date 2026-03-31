"""Helper-facing client boundary for future node-helper integration."""

from __future__ import annotations

from typing import Protocol

from app.backends.helper_adapter import HelperAdapterStub
from app.backends.helper_protocol import HelperCommandRequest, HelperCommandResult


class HelperClient(Protocol):
    """Boundary contract for helper command execution."""

    def execute(self, request: HelperCommandRequest) -> HelperCommandResult:
        """Execute a helper command request and return protocol result."""


class StubHelperClient:
    """Deterministic helper client backed by ``HelperAdapterStub``.

    This client exposes a helper-facing boundary while the project remains in
    protocol/adapter stage and does not run real helper transports.
    """

    def __init__(self, adapter: HelperAdapterStub | None = None) -> None:
        self._adapter = adapter or HelperAdapterStub()

    def execute(self, request: HelperCommandRequest) -> HelperCommandResult:
        """Delegate execution to deterministic in-process helper adapter."""
        return self._adapter.execute(request)


class ProcessHelperClient:
    """Placeholder for future real helper transport integration.

    TODO: Implement subprocess or IPC transport boundary to real node-helper.
    TODO: Keep bot process free from direct runtime/system command execution.
    """

    def execute(self, request: HelperCommandRequest) -> HelperCommandResult:
        raise NotImplementedError("Process helper client transport is not implemented yet")
