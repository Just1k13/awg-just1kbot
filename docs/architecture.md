# Architecture

## In scope now
- Telegram bot runtime skeleton with aiogram.
- Typed environment configuration.
- Async SQLAlchemy and migration setup.
- Minimal domain model and repository skeletons.
- Backend abstraction for future AWG integration.

## Out of scope now
- Any payment/Telegram Stars logic.
- Referral and anti-abuse mechanics.
- Real AWG peer operations.
- Multi-node orchestration logic.
- Web UI, Redis, and task queues.

## Layout
- `bot/`: bot entrypoint and handlers.
- `app/config/`: typed settings from env.
- `app/db/`: ORM models, session setup, repositories.
- `app/backends/`: backend interface and AWG stub.
- `docs/`: project architecture and roadmap.

## Development direction
1. Add single-node backend implementation.
2. Add subscription flows.
3. Add profile generation and export flow.
4. Add second node support without orchestration overreach.
