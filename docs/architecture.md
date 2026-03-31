# Architecture

## Current stage
Foundation + backend contract.

## In scope now
- Telegram bot runtime skeleton with aiogram.
- Typed environment configuration.
- Async SQLAlchemy and migration setup.
- Minimal domain model and repository skeletons.
- Minimal AWG backend contract and kernel backend stub (no runtime logic).
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
- `docs/`: project architecture, roadmap, and helper contract draft.

## Development direction
1. Single-node kernel integration.
2. Subscription flows.
3. Profile generation and export.
4. Second node support.
5. Anti-abuse controls.
6. Referrals.
