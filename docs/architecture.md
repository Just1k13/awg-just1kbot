# Architecture

## Current stage
Foundation + helper contract + app-level preflight + read-only integration planning.

## In scope now
- Telegram bot runtime skeleton with aiogram.
- Typed environment configuration.
- Async SQLAlchemy and migration setup.
- Minimal domain model and repository skeletons.
- Minimal AWG backend contract and kernel backend stub (no runtime logic).
- Application-level single-node preflight checks.
- Read-only runtime inspection service skeleton.
- Draft documentation for future node-helper boundary.

## Out of scope now
- Any payment/Telegram Stars logic.
- Referral and anti-abuse mechanics.
- Real AWG peer operations.
- Node-helper implementation.
- Multi-node orchestration logic.
- Web UI, Redis, and task queues.

## Layout
- `bot/`: bot entrypoint and handlers.
- `app/config/`: typed settings from env.
- `app/db/`: ORM models, session setup, repositories.
- `app/backends/`: backend contract and kernel AWG stub.
- `app/services/node_preflight.py`: application-level preflight for default single-node runtime.
- `app/services/runtime_inspection.py`: read-only runtime inspection orchestration.
- `docs/`: architecture, roadmap, and helper contract draft.

## Development direction
1. Minimal safe helper-facing wiring (or protocol draft).
2. Subscription flows.
3. Profile generation and export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
