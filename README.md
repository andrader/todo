# Todo App

A simple personal Todo application built with Python and Streamlit for local task management.

## Features
- **Task Management**: Create, Read, Update, Delete (CRUD) tasks.
- **Details**: Support for Task Title and optional Description.
- **Status**: Mark tasks as Completed or Active.
- **Filtering**: View All, Active, or Completed tasks.
- **Persistence**: Data is saved locally using SQLite (`todo.db`), surviving restarts.
- **Validation**: Robust data handling with Pydantic.

## Setup & Running

### Prerequisites
- Python 3.13+
- `uv` package manager (recommended) or `pip`

### Installation

1. **Install uv** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Install Dependencies**:
   ```bash
   uv sync
   ```

### Running the App

Run the Streamlit application:
```bash
uv run streamlit run src/todo/app.py
```
The app will open in your default browser (usually at `http://localhost:8501`).

## Development

### Run Tests
Execute the test suite using `pytest`:
```bash
uv run pytest
```

### Linting
Check code quality with `ruff`:
```bash
uv run ruff check .
```

## Scope & Known Limitations

**Implemented Features:**
- ✅ Create tasks (Title + Description)
- ✅ List tasks
- ✅ Mark as completed/active
- ✅ Edit tasks (Title + Description)
- ✅ Delete tasks
- ✅ Persistence (SQLite)
- ✅ Task Filtering (All/Active/Completed)
- ✅ Unit Tests & CI/CD

**Not Implemented (Optional):**
- ❌ Due dates / reminders
- ❌ Priority or tags
- ❌ Search bar (Filtering provided instead)
- ❌ Categories or grouping
- ❌ Natural-language input

**Limitations:**
- Local storage only (SQLite file created in the running directory).
- Single-user application (no authentication).
