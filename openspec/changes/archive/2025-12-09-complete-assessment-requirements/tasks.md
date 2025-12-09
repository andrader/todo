## 1. CI/CD Implementation
- [x] 1.1 Create `.github/workflows/CI.yml` with steps for `uv` setup, linting, and testing.
- [x] 1.2 Verify CI configuration locally (if possible) or ensure correctness against GitHub Actions docs.

## 2. UI Enhancements
- [x] 2.1 Update `src/todo/app.py`: Add "Description" input to the "Add Todo" form.
- [x] 2.2 Update `src/todo/app.py`: Add tabs or radio buttons for Filtering (All/Active/Completed).
- [x] 2.3 Update `src/todo/app.py`: Implement an "Edit" mode (e.g., using `st.expander` or a dialog) to update Title and Description.
- [x] 2.4 Update `src/todo/app.py`: Display Description alongside Title.

## 3. Documentation & Deliverables
- [x] 3.1 Update `README.md`: Add "Scope & Known Limitations" section explicitly listing implemented vs. optional features.
- [x] 3.2 Create `metadata.txt`: Fill in Time Spent, AI Tools, Features Implemented/Not Implemented.
- [x] 3.3 Verify `README.md` has clear commands for Install, Run, and Test (already started, but double-check).

## 4. Final Verification
- [x] 4.1 Run full linting (`uv run ruff check .`).
- [x] 4.2 Run full testing (`uv run pytest`).
- [x] 4.3 Manual UI walkthrough to ensure all "Required Features" are visible and functional.
