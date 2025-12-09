.PHONY: install format lint lint-fix test all

install:
	uv sync

format:
	uv run ruff format .

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

test:
	uv run pytest

all: format lint-fix test

