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
Protocol draft + in-process deterministic adapter stub.

- Runtime helper process is **not implemented**.
- Runtime commands are **not executed** by the app yet.
- No IPC/transport implementation exists (no HTTP, JSON-RPC, Unix socket, subprocess wiring).
- `app/backends/helper_adapter.py` provides deterministic in-process responses for read-only DTOs.

## Read-only protocol draft in this phase
The repository now includes `app/backends/helper_protocol.py` with request/result envelopes
for read-only command interaction shape.

Read-only command DTO scope:
- `healthcheck`
- `peer-show`
- `peer-list`
- `config-render`

Mutation commands remain in `HelperCommand` contract only and are intentionally not expanded
into transport DTOs in this phase.

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
Add an explicit helper-facing client/gateway boundary on top of the current adapter stub,
still without executing real node/system commands.

## Responsibility boundaries
- **bot**: Telegram interaction and user flow orchestration.
- **app (service/backend layer)**: domain decisions, persistence, and helper command orchestration.
- **backend contract**: runtime-agnostic interface for AWG operations.
- **helper (future)**: privileged execution of AWG/tools commands.
- **node**: actual kernel/runtime where peer state lives.
