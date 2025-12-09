# Todo App

A simple personal Todo application built with Python and Streamlit for local task management.

## Features
- **Task Management**: Create, Read, Update, Delete (CRUD) tasks.
- **Rich Details**: Support for Title, Description, **Due Dates**, **Priority**, and **Categories**.
- **Smart Input**: **Natural Language Processing (NLP)** allows adding tasks like "Buy milk tomorrow !high #personal".
- **Status**: Mark tasks as Completed or Active.
- **Advanced Filtering**: Filter by Status, **Search**, **Priority**, and **Category**.
- **Sorting**: Smart sorting by status, due date, and priority.
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

### Makefile Commands
The project includes a `Makefile` to simplify common development tasks:

- `make install`: Install dependencies using `uv sync`.
- `make test`: Run the test suite.
- `make lint`: Check for linting errors.
- `make lint-fix`: Check and automatically fix linting errors.
- `make format`: Format code using `ruff`.
- `make all`: Run formatting, lint fixing, and tests in sequence.

### Run Tests
Execute the test suite using `pytest`:
```bash
uv run pytest
```
or simply:
```bash
make test
```

### Linting
Check code quality with `ruff`:
```bash
uv run ruff check .
```
or:
```bash
make lint
```

## Scope & Known Limitations

**Implemented Features:**
- ✅ Create tasks (Title, Description, Due Date, Priority, Category)
- ✅ List tasks with sorting
- ✅ Mark as completed/active
- ✅ Edit tasks (All fields)
- ✅ Delete tasks
- ✅ Persistence (SQLite)
- ✅ Advanced Filtering (Search, Status, Priority, Category)
- ✅ Natural Language Input (Quick Add)
- ✅ Unit Tests & CI/CD

**Not Implemented:**
- ❌ Keyboard shortcuts (Native browser/form submission supported, but no global hotkeys)
- ❌ Drag-and-drop reordering

**Limitations:**
- Local storage only (SQLite file created in the running directory).
- Single-user application (no authentication).
