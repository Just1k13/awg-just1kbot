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
### Read-only commands (next implementation focus)
- `healthcheck` — node health snapshot.
- `peer-show` — runtime snapshot for one peer.
- `peer-list` — runtime snapshots for all peers on node.
- `config-render` — client config export content/metadata.

### Later mutation commands
- `peer-add`
- `peer-disable`
- `peer-delete`
- `reconcile`

## Expected response shapes (planning-level)
- `healthcheck` -> `{ ok: bool, detail?: str, checked_at?: datetime }`
- `peer-show` -> `{ enabled: bool, last_handshake_at?: datetime, rx_bytes?: int, tx_bytes?: int, endpoint?: str }`
- `peer-list` -> `list[peer-show shape]`
- `config-render` -> `{ content: str, metadata: { file_name: str, content_type: str } }`
- `reconcile` -> later-only command, no shape fixed in this phase

## Scope in this PR
Node-helper is **not** implemented in this PR.
This PR only defines read-only and mutation command boundaries, expected result shapes,
and keeps backend/service layers ready for safe helper-facing wiring.

## Responsibility boundaries
- **bot**: Telegram interaction and user flow orchestration.
- **app (service/backend layer)**: domain decisions, persistence, and helper command orchestration.
- **backend contract**: runtime-agnostic interface for AWG operations.
- **helper (future)**: privileged execution of AWG/tools commands.
- **node**: actual kernel/runtime where peer state lives.
