## Context
The assessment suggests optional features including "Due dates", "Priority", "Filters", "Categories", "Natural-language input", and "Keyboard shortcuts".

## Decisions

### Data Model
- `due_date`: Stored as ISO 8601 string or SQLite compatible date/datetime. Python `datetime`.
- `priority`: Enum or String (`High`, `Medium`, `Low`). Default `Medium`.
- `category`: String. User defined or fixed list. We will allow free-text categories for flexibility.

### Natural Language Input
- We MUST use `dateparser` library for robust date parsing.
- Pattern: "Task title [at/on date] [priority] [#category]".
- Example: "Buy milk tomorrow at 5pm !high #personal".

### UI Filters
- Sidebar is the best place for persistent filters.
- Filters will be additive (AND logic).

### Keyboard Shortcuts
- Streamlit has limited support for custom global shortcuts.
- We will focus on:
  - Form submission (Command/Ctrl + Enter) which is native to `st.form`.

## Trade-offs
- **NLP vs Structured Input**: We will offer *both*. A "Quick Add" (NLP) and a "Detailed Add" (Form). This covers power users and casual users.
- **Migration**: We will drop/recreate the database schema as there is no production data to preserve. This simplifies the implementation.

## Open Questions
- None at this stage.

