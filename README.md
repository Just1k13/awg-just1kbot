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

## Local development

### 1) Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
make install-dev
```

### 3) Create local environment file
```bash
cp .env.example .env
```

### 4) Start PostgreSQL locally
You can use any local PostgreSQL instance.

Option A: local service (example)
```bash
createdb awg_bot
```

Option B: only PostgreSQL via docker compose
```bash
docker compose -f docker-compose.dev.yml up -d
```

### 5) Apply migrations
```bash
make alembic-upgrade
```

### 6) Run bot
```bash
make run-bot
```

### 7) Run quality checks and tests
```bash
make lint
make test
```
