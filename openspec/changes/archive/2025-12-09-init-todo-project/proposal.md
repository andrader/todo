# Change: Initialize Todo Project Structure

## Why
To start the development of the personal Todo application, we need to establish the project skeleton, dependency management, data validation, and persistence layer. This foundation ensures a robust and maintainable codebase from the beginning.

## What Changes
- Initialize Python project using `uv`.
- Set up SQLite database for persistence.
- Implement Pydantic models for data validation.
- Create basic project structure for source code and tests.
- Define core Todo management requirements.

## Impact
- **Specs**: New `core` capability for Todo management.
- **Code**: Creation of `pyproject.toml`, `src/todo/`, `tests/`.
- **Dependencies**: Adds `pydantic` and `pytest`.

