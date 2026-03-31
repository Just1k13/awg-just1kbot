PYTHON ?= python

.PHONY: install-dev lint typecheck test migrate-up migrate-down bot

install-dev:
	$(PYTHON) -m pip install -e .[dev]

lint:
	ruff check .

typecheck:
	mypy app bot tests

test:
	pytest

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1

bot:
	$(PYTHON) -m bot.main
