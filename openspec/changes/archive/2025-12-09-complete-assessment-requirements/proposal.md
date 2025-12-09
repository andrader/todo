# Change: Complete Assessment Requirements

## Why
The initial project scaffolding (`init-todo-project`) established the core backend and a basic UI. However, the `assessment-context.md` specifies additional mandatory requirements that are currently missing, specifically regarding UI features (filtering, editing), CI/CD automation, and strict documentation deliverables. This change aims to bridge that gap and ensure full compliance with the assessment.

## What Changes
- **UI Implementation (`src/todo/app.py`):**
    - Add "Description" field to the creation form.
    - Implement "Edit" functionality for Task Title and Description.
    - Implement Task Filtering (All, Active, Completed).
    - Display Task Description in the list view.
- **CI/CD (`.github/workflows/CI.yml`):**
    - Create a GitHub Actions workflow that runs on Ubuntu.
    - Workflow steps: Checkout, Install `uv` & dependencies, Lint (ruff/flake8), Run Tests (`pytest`).
- **Documentation (`README.md`, `metadata.txt`):**
    - Update `README.md` to include the mandatory "Scope & Known Limitations" section.
    - Create `metadata.txt` with time spent, tools used, and feature status.
    - Ensure `README.md` has clear Test and Run instructions.

## Impact
- **Specs**: Adds `ui`, `ci`, and `documentation` capabilities.
- **Code**: Modifies `src/todo/app.py`, adds `.github/workflows/CI.yml`, adds `metadata.txt`.
- **User Experience**: Users can now filter tasks and edit them, matching standard Todo app expectations.

