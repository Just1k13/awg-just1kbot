# awg-just1kbot

Production-minded foundation for a future Telegram bot that manages access in an AWG-based setup.

## Current scope (implemented)
- Clean project structure for bot, domain, db, and docs.
- Typed environment-based settings (Pydantic v2).
- SQLAlchemy 2.x async database foundation.
- Alembic migration environment with an initial migration.
- Minimal domain models for future access-management flows.
- Minimal aiogram bot foundation with `/start` and `/help`.
- Backend abstraction layer for AWG runtime integration (`app/backends`).
- Basic quality tooling setup: pytest, Ruff, mypy, Makefile.

## Intentionally out of scope (not implemented)
- Real integration with `amneziawg-linux-kernel-module` / `amneziawg-tools`.
- Real AWG peer lifecycle operations.
- Node-helper implementation.
- Payments and Telegram Stars.
- Referral/reward system.
- Anti-abuse logic.
- Multi-node orchestration business logic.
- Redis/task queues/web UI.

See `TODO.md`, `docs/architecture.md`, `docs/node-helper.md`, and `docs/roadmap.md`.

## Quick start
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   make install-dev
   ```
3. Copy environment template and edit values:
   ```bash
   cp .env.example .env
   ```

## Run migrations
```bash
make migrate-up
```

## Run bot locally
```bash
make bot
```

## Run checks
```bash
make lint
make typecheck
make test
```

## Short roadmap
- Phase 0: scaffold cleanup
- Phase 1: single-node kernel integration
- Phase 2: subscription flows
- Phase 3: profile generation/export
- Phase 4: second node support
- Phase 5+: hardening and extended capabilities
