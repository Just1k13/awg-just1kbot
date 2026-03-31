# Architecture

## Current stage
Foundation + backend boundary + single-node preflight + helper protocol DTOs + deterministic adapter stub + helper-facing client boundary + read-only and mutation kernel backend wiring + runtime inspection foundation.

## In scope now
- Telegram bot runtime skeleton with aiogram.
- Typed environment configuration.
- Async SQLAlchemy and migration setup.
- Minimal domain model and repository skeletons.
- Minimal AWG backend contract and kernel backend wiring through helper client.
- Application-level single-node preflight checks.
- Helper protocol DTOs for read-only and mutation commands (`app/backends/helper_protocol.py`).
- Deterministic helper adapter stub for read-only and mutation commands (`app/backends/helper_adapter.py`).
- Helper-facing client boundary with stub + real-client skeleton (`app/backends/helper_client.py`).
- `KernelAwgBackend` methods wired through `HelperClient` and protocol DTOs.
- Runtime inspection service (`app/services/runtime_inspection.py`) aligned to backend read-only contract.
- Draft documentation for future node-helper boundary.

## Out of scope now
- Any payment/Telegram Stars logic.
- Referral and anti-abuse mechanics.
- Real AWG peer operations.
- Node-helper implementation.
- Runtime command execution from the app process.
- IPC/transport implementation for helper communication.
- Multi-node orchestration logic.
- Web UI, Redis, and task queues.

## Layout
- `bot/`: bot entrypoint and handlers.
- `app/config/`: typed settings from env.
- `app/db/`: ORM models, session setup, repositories.
- `app/backends/`: backend contract, helper command/protocol drafts, adapter/client stubs, and kernel AWG backend.
- `app/services/node_preflight.py`: application-level preflight for default single-node runtime.
- `docs/`: project architecture, roadmap, and helper contract draft.

## Development direction
1. Real helper transport boundary design/implementation (process/IPC contract and serialization layer).
2. Subscription flows.
3. Profile generation and export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
