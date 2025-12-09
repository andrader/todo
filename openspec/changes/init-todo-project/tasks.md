## 1. Project Setup
- [ ] 1.1 Initialize project with `uv init --package --app`.
- [ ] 1.2 Add dependencies: `uv add pydantic streamlit` and dev dependencies `uv add --dev pytest ruff`.
- [ ] 1.3 Create `README.md` with setup and usage instructions.

## 2. Core Logic Implementation
- [ ] 2.1 Create `src/todo/models.py` with Pydantic models (`Todo`, `TodoCreate`, `TodoUpdate`).
- [ ] 2.2 Create `src/todo/db.py` with SQLite connection and table initialization logic.
- [ ] 2.3 Implement CRUD operations in `src/todo/repository.py` (or `db.py`): `add_todo`, `get_todos`, `update_todo`, `delete_todo`.

## 3. Testing
- [ ] 3.1 Create `tests/test_models.py` to validate Pydantic models.
- [ ] 3.2 Create `tests/test_db.py` to test persistence operations (using in-memory SQLite).

## 4. UI Skeleton
- [ ] 4.1 Create basic `src/todo/app.py` to verify dependencies and DB connection work.

