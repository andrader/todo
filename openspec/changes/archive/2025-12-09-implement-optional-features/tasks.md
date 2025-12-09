## 1. Data Layer & Core Logic
- [x] 1.1 Add `dateparser` to `pyproject.toml` and install dependencies.
- [x] 1.2 Update `Task` model in `src/todo/models.py` to include `due_date`, `priority`, `category`.
- [x] 1.3 Update database schema in `src/todo/db.py` (drop/recreate logic since no data).
- [x] 1.4 Create `src/todo/nlp.py` using `dateparser` to extract dates and regex for priority/category.
- [x] 1.5 Update repository in `src/todo/repository.py` to handle new fields.
- [x] 1.6 Update tests in `tests/` to cover new fields and NLP logic.

## 2. User Interface
- [x] 2.1 Update Sidebar in `src/todo/app.py` to include Search input, Category filter, and Priority filter.
- [x] 2.2 Update Task List display to show Due Date, Priority badge, and Category.
- [x] 2.3 Implement sorting logic (e.g., sort by Due Date, then Priority).
- [x] 2.4 Update "Add Task" form to allow optional manual entry of new fields OR use the NLP input.
- [x] 2.5 Add keyboard shortcut support (e.g., `Ctrl+Enter` to submit active form) if feasible in Streamlit.

## 3. Documentation
- [x] 3.1 Update `README.md` to list new features.
- [x] 3.2 Update `metadata.txt` to reflect implemented optional features.
