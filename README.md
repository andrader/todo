# Todo App

A simple personal Todo application built with Python and Streamlit.

## Features
- Create, Read, Update, Delete (CRUD) Todos.
- Persistence using SQLite.
- Data validation using Pydantic.

## Setup

1. **Install uv**:
   ```bash
   pip install uv
   ```

2. **Initialize and Install Dependencies**:
   ```bash
   uv sync
   ```

3. **Run the Application**:
   ```bash
   uv run streamlit run src/todo/app.py
   ```

## Development

- **Run Tests**:
  ```bash
  uv run pytest
  ```
- **Lint**:
  ```bash
  uv run ruff check .
  ```

