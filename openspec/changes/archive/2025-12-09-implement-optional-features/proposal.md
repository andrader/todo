# Change: Implement Optional Features

## Why
The project assessment includes a set of optional features ("nice-to-haves") that demonstrate deeper engineering capability and user empathy. Implementing these features will make the application more practical for real-world use and fulfill the "extra credit" portion of the assessment.

## What Changes
- **Data Model**: specific fields added to `Task`: `due_date`, `priority`, `category`.
- **UI/UX**: 
  - Enhanced "Add Task" with Natural Language Processing (NLP) capabilities.
  - Sidebar with advanced filters (Search, Priority, Category).
  - Visual indicators for high priority and overdue tasks.
- **Logic**: Simple NLP parser to extract dates and priorities from text input.

## Impact
- **Specs**: `core` (data model), `ui` (filtering, input).
- **Code**: `pyproject.toml` (deps), `models.py` (schema), `app.py` (UI), new `nlp.py` (parsing), `db.py`.

