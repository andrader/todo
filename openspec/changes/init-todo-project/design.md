# Design: Project Initialization and Architecture

## Context
The project requires a local Todo application with persistence. We are choosing a modern Python stack to ensure developer productivity and code quality.

## Goals / Non-Goals
- **Goals**:
    - Fast and reliable package management.
    - Type-safe data handling.
    - Zero-config persistence (local file).
- **Non-Goals**:
    - Multi-user support (local only).
    - Remote database synchronization.

## Decisions

### 1. Package Management: `uv`
- **Decision**: Use `uv` for project initialization and dependency management.
- **Why**: It provides a fast, unified toolchain for Python projects (`init`, `sync`, `run`).
- **Command**: `uv init --package --app` to set up a library-style layout with an application entry point.

### 2. Persistence: SQLite
- **Decision**: Use `sqlite3` (standard library).
- **Why**:
    - Embedded, serverless, and zero-configuration.
    - Reliable ACID compliance.
    - Single file storage makes it easy to backup or move.
- **Schema**:
    - Table `todos`:
        - `id`: TEXT (UUID) or INTEGER PK
        - `title`: TEXT NOT NULL
        - `description`: TEXT
        - `completed`: BOOLEAN DEFAULT 0
        - `created_at`: DATETIME DEFAULT CURRENT_TIMESTAMP

### 3. Data Validation: Pydantic
- **Decision**: Use Pydantic V2.
- **Why**:
    - Industry standard for Python data validation.
    - Runtime type checking.
    - Easy serialization/deserialization to/from JSON/Dicts for the UI and DB layers.
- **Models**:
    - `TodoCreate`: Input model (title, description).
    - `TodoUpdate`: Update model (title, description, completed).
    - `Todo`: Domain model (includes id, created_at).

## Risks / Trade-offs
- **SQLite Concurrency**: Not an issue for a single-user local app.
- **Migration**: No complex migration tool (like Alembic) initially; we will recreate the DB file if schema changes during early dev.

## Open Questions
- None.

