# AGENTS instructions

These rules apply to the entire repository.

## Delivery style
- Keep changes small, reviewable, and scoped to the current task.
- Prefer simple, maintainable solutions over abstract frameworks.
- Do not add product features outside the current scope.
- If requirements are unclear, add a TODO and stop instead of inventing business logic.

## Architecture and runtime
- Security first: never hardcode secrets or credentials.
- Do not assume the bot runs with root privileges.
- Do not couple runtime behavior to Docker.
- Avoid speculative abstractions and "future-proof" layers that are not needed now.

## Quality bar
- Keep code and docs in English.
- Run relevant tests/linters when changing code.
- Avoid dead code and commented-out blocks.
