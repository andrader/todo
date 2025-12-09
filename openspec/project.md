# Project Context

## Purpose
A personal TODO / Checklist application for local use. The goal is to provide a simple, persistent way to manage tasks with basic CRUD operations, demonstrating end-to-end software engineering practices including testing, CI/CD, and documentation.

## Tech Stack
- **Language:** Python 3
- **Framework:** Streamlit (Full-stack UI)
- **Persistence:** JSON or SQLite (Local file storage)
- **Package Manager:** `uv` (recommended) or `pip`
- **Testing:** `pytest`
- **Linting:** `flake8`, `ruff`, or `black`

## Project Conventions

### Code Style
- Follow PEP 8 guidelines.
- Use `black` for code formatting.
- Use `ruff` or `flake8` for linting.
- Type hints are encouraged.

### Architecture Patterns
- **Presentation Layer:** Streamlit for the frontend UI.
- **Data Layer:** A dedicated module for handling persistence (reading/writing to JSON/SQLite) to separate concerns from the UI.
- **State Management:** Leverage Streamlit's `st.session_state` for transient UI state, while committing changes to disk for persistence.

### Testing Strategy
- **Framework:** `pytest`.
- **Scope:** Unit tests for data persistence and core logic (CRUD).
- **CI/CD:** Tests and linting must run and pass on GitHub Actions (Ubuntu runner) for every push/PR.

### Git Workflow
- Simple feature branch workflow.
- Commits should be atomic and descriptive.
- CI pipeline acts as the quality gate.

## Domain Context
- **Task:** The core entity, consisting of:
  - `title` (Required)
  - `description` (Optional)
  - `completed` (Boolean status)
- **Persistence:** Data MUST survive application restarts.

## Important Constraints
- **Time:** ~60 minutes coding time expectation.
- **Scope:** Focus on "Required Features" first: Create, List, Complete/Uncomplete, Edit, Delete, Persistence.
- **Documentation:** `README.md` must be comprehensive (Setup, Run, Test, Scope/Limitations). `metadata.txt` is required for submission.

## External Dependencies
- **GitHub Actions:** Required for the CI workflow.
