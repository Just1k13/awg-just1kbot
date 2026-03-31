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
Protocol draft + helper-facing adapter stub.

- Runtime helper process is **not implemented**.
- Runtime/system commands are **not executed** by the app.
- No IPC/transport implementation exists (no HTTP, JSON-RPC, Unix socket, subprocess wiring).

## Read-only protocol + adapter stub in this phase
The repository includes:
- `app/backends/helper_protocol.py` for request/result envelopes and read-only DTO shape.
- `app/backends/helper_adapter.py` for deterministic in-process stub handling.

Read-only command scope:
- `healthcheck`
- `peer-show`
- `peer-list`
- `config-render`

Mutation commands remain in `HelperCommand` contract only and are intentionally not expanded
into transport/adapter execution in this phase.

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
Swap the stub adapter for a real helper-facing implementation boundary while preserving the
same protocol DTO shape and keeping system execution isolated behind that boundary.

## Responsibility boundaries
- **bot**: Telegram interaction and user flow orchestration.
- **app (service/backend layer)**: domain decisions, persistence, and helper command orchestration.
- **backend contract**: runtime-agnostic interface for AWG operations.
- **helper (future)**: privileged execution of AWG/tools commands.
- **node**: actual kernel/runtime where peer state lives.
