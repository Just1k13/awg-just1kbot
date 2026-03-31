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

## Planned helper commands
- `peer-add`
- `peer-disable`
- `peer-delete`
- `peer-show`
- `peer-list`
- `config-render`
- `reconcile`

These commands are contract targets for future implementation and may evolve minimally
as runtime integration work starts.

## Scope in this PR
Node-helper is **not** implemented in this PR.
This PR only introduces backend interfaces/stubs and documents expected helper boundaries.

## Responsibility boundaries
- **bot**: Telegram interaction and user flow orchestration.
- **app (service/backend layer)**: domain decisions, persistence, and helper command orchestration.
- **backend contract**: runtime-agnostic interface for AWG operations.
- **helper (future)**: privileged execution of AWG/tools commands.
- **node**: actual kernel/runtime where peer state lives.
