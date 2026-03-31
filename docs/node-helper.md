# Node helper contract (draft)

## Why helper is needed
The bot application should not execute privileged kernel networking operations directly.
Future AWG runtime operations require access typically restricted to root/system-level capabilities.
A dedicated helper process will isolate privileged execution from bot business logic.

## Security boundary
- Bot/app layer runs with regular service permissions.
- Bot/app layer must not require root privileges.
- Helper is the only component allowed to perform privileged AWG/kernel calls.
- Node host remains the source of truth for runtime state.

## Current stage
Protocol DTOs + in-process deterministic adapter stub + helper-facing client boundary + read-only and mutation backend wiring.

- Runtime helper process is **not implemented**.
- Runtime commands are **not executed** by the app yet.
- No IPC/transport implementation exists (no HTTP, JSON-RPC, Unix socket, subprocess wiring).
- `app/backends/helper_adapter.py` provides deterministic in-process responses for read-only and mutation DTOs.
- `app/backends/helper_client.py` defines helper-facing boundary contract and a stub client that delegates to the adapter.
- `app/backends/kernel_awg.py` routes backend methods through `HelperClient` and protocol envelopes.
- Failed helper results are surfaced as backend-level errors (no silent fallback path).

## Protocol DTO scope in this phase
The repository includes `app/backends/helper_protocol.py` with request/result envelopes and typed payload DTOs.

Read-only command DTOs:
- `healthcheck`
- `peer-show`
- `peer-list`
- `config-render`

Mutation command DTOs:
- `peer-add`
- `peer-disable`
- `peer-delete`
- `reconcile`

`reconcile` is currently prepared at protocol/client/adapter level as the next operational command,
but not yet exposed as a dedicated backend API method.

## Planned helper commands (full contract target)
- `peer-add`
- `peer-disable`
- `peer-delete`
- `peer-show`
- `peer-list`
- `config-render`
- `reconcile`
- `healthcheck`

## Next step
Implement real helper transport boundary (process/IPC) behind `HelperClient` while still keeping
app process free from direct runtime/system command execution.

## Responsibility boundaries
- **bot**: Telegram interaction and user flow orchestration.
- **app (service/backend layer)**: domain decisions, persistence, and helper command orchestration.
- **backend contract**: runtime-agnostic interface for AWG operations.
- **helper (future)**: privileged execution of AWG/tools commands.
- **node**: actual kernel/runtime where peer state lives.
