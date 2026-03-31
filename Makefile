PYTHON ?= python

.PHONY: install-dev lint ruff-check test run-bot alembic-upgrade alembic-revision

install-dev:
	$(PYTHON) -m pip install -e .[dev]

lint: ruff-check

ruff-check:
	ruff check .

test:
	pytest

run-bot:
	$(PYTHON) -m bot.main

alembic-upgrade:
	alembic upgrade head

alembic-revision:
	alembic revision --autogenerate -m "$(m)"
