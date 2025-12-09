## Context
The assessment requires a specific set of features and deliverables. While the backend supports them, the current UI is minimal. We need to expand the UI without introducing unnecessary complexity (like complex routing), keeping it a single-page Streamlit app.

## Goals
- Full compliance with `assessment-context.md`.
- Simple, intuitive UI using standard Streamlit widgets.
- Zero-config CI pipeline.

## Decisions
- **UI Pattern**: Use Streamlit's `st.tabs` for filtering (All, Active, Completed) as it provides a clean switching mechanism.
- **Edit Pattern**: Use `st.expander` or a conditional rendering block for editing. Since Streamlit reruns on interaction, an in-place edit might be tricky. A simpler approach is an "Edit" button that opens a form (perhaps in a dialog/modal `st.dialog` if available in the installed version, or just a form appearing below/replacing the row). *Decision*: Use `st.expander` per task for details, with an edit form inside it. This keeps the list clean.
- **CI Provider**: GitHub Actions, as mandated.

## Risks
- **Time Constraint**: The assessment suggests ~60 minutes. We need to implement these UI changes quickly.
- **Streamlit State**: editing lists in Streamlit can be tricky with keys. We must ensure unique keys for all widgets (e.g., `key=f"edit_{todo.id}"`).

## Open Questions
- None. Requirements are clear from `assessment-context.md`.

