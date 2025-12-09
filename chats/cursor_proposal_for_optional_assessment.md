# Proposal for optional assessment features
_Exported on 12/8/2025 at 23:06:03 GMT-3 from Cursor (2.1.50)_

---

**User**

/openspec-proposal proposal to implement the optional features in @assessment-context.md 

--- Cursor Command: openspec-proposal.md ---
---
name: /openspec-proposal
id: openspec-proposal
category: OpenSpec
description: Scaffold a new OpenSpec change and validate strictly.
---
<!-- OPENSPEC:START -->
**Guardrails**
- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Refer to `openspec/AGENTS.md` (located inside the `openspec/` directory—run `ls openspec` or `openspec update` if you don't see it) if you need additional OpenSpec conventions or clarifications.
- Identify any vague or ambiguous details and ask the necessary follow-up questions before editing files.
- Do not write any code during the proposal stage. Only create design documents (proposal.md, tasks.md, design.md, and spec deltas). Implementation happens in the apply stage after approval.

**Steps**
1. Review `openspec/project.md`, run `openspec list` and `openspec list --specs`, and inspect related code or docs (e.g., via `rg`/`ls`) to ground the proposal in current behaviour; note any gaps that require clarification.
2. Choose a unique verb-led `change-id` and scaffold `proposal.md`, `tasks.md`, and `design.md` (when needed) under `openspec/changes/<id>/`.
3. Map the change into concrete capabilities or requirements, breaking multi-scope efforts into distinct spec deltas with clear relationships and sequencing.
4. Capture architectural reasoning in `design.md` when the solution spans multiple systems, introduces new patterns, or demands trade-off discussion before committing to specs.
5. Draft spec deltas in `changes/<id>/specs/<capability>/spec.md` (one folder per capability) using `## ADDED|MODIFIED|REMOVED Requirements` with at least one `#### Scenario:` per requirement and cross-reference related capabilities when relevant.
6. Draft `tasks.md` as an ordered list of small, verifiable work items that deliver user-visible progress, include validation (tests, tooling), and highlight dependencies or parallelizable work.
7. Validate with `openspec validate <id> --strict` and resolve every issue before sharing the proposal.

**Reference**
- Use `openspec show <id> --json --deltas-only` or `openspec show <spec> --type spec` to inspect details when validation fails.
- Search existing requirements with `rg -n "Requirement:|Scenario:" openspec/specs` before writing new ones.
- Explore the codebase with `rg <keyword>`, `ls`, or direct file reads so proposals align with current implementation realities.
<!-- OPENSPEC:END -->

--- End Command ---

---

**Cursor**

```markdown
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
- **Code**: `models.py` (schema), `app.py` (UI), new `nlp.py` (parsing logic), `db.py` (migrations).

```

```markdown
## 1. Data Layer & Core Logic
- [ ] 1.1 Update `Task` model in `src/todo/models.py` to include `due_date`, `priority`, `category`.
- [ ] 1.2 Update database schema in `src/todo/db.py` to support new columns (handle migration or recreation).
- [ ] 1.3 Create `src/todo/nlp.py` to parse natural language strings (e.g., "Buy milk tomorrow") into task data.
- [ ] 1.4 Update repository in `src/todo/repository.py` to handle new fields.
- [ ] 1.5 Update tests in `tests/` to cover new fields and NLP logic.

## 2. User Interface
- [ ] 2.1 Update Sidebar in `src/todo/app.py` to include Search input, Category filter, and Priority filter.
- [ ] 2.2 Update Task List display to show Due Date, Priority badge, and Category.
- [ ] 2.3 Implement sorting logic (e.g., sort by Due Date, then Priority).
- [ ] 2.4 Update "Add Task" form to allow optional manual entry of new fields OR use the NLP input.
- [ ] 2.5 Add keyboard shortcut support (e.g., `Ctrl+Enter` to submit active form) if feasible in Streamlit.

## 3. Documentation
- [ ] 3.1 Update `README.md` to list new features.
- [ ] 3.2 Update `metadata.txt` to reflect implemented optional features.

```

```markdown
## Context
The assessment suggests optional features including "Due dates", "Priority", "Filters", "Categories", "Natural-language input", and "Keyboard shortcuts".

## Decisions

### Data Model
- `due_date`: Stored as ISO 8601 string or SQLite compatible date/datetime. Python `datetime`.
- `priority`: Enum or String (`High`, `Medium`, `Low`). Default `Medium`.
- `category`: String. User defined or fixed list. We will allow free-text categories for flexibility.

### Natural Language Input
- We will implement a lightweight parser (likely regex-based + `dateparser` library if allowed, or simple `datetime` logic) to avoid heavy ML dependencies.
- Pattern: "Task title [at/on date] [priority] [#category]" or similar.
- If `dateparser` is too heavy, we will support basic keywords like "today", "tomorrow", "next week".

### UI Filters
- Sidebar is the best place for persistent filters.
- Filters will be additive (AND logic).

### Keyboard Shortcuts
- Streamlit has limited support for custom global shortcuts.
- We will focus on:
  - Form submission (Command/Ctrl + Enter) which is native to `st.form`.
  - Potentially a quick "Focus Add Task" button if possible, but standard browser tab navigation is the fallback.

## Trade-offs
- **NLP vs Structured Input**: We will offer *both*. A "Quick Add" (NLP) and a "Detailed Add" (Form). This covers power users and casual users.
- **Migration**: Since this is a local single-user app, we might check if the DB columns exist on startup and add them if missing, or simply advise deleting `todo.db` if schema changes are too complex for a simple exercise (though migration is better engineering practice). We will attempt `ALTER TABLE` if possible.

## Open Questions
- None at this stage.

```

```markdown
## MODIFIED Requirements
### Requirement: Todo Management
The system SHALL provide capabilities to manage Todo items with rich metadata.

#### Scenario: Create a new Todo
- **WHEN** a user submits a task with a title and optional details (description, due date, priority, category)
- **THEN** the task is persisted with all provided attributes
- **AND** `completed` is set to false by default

#### Scenario: List Todos
- **WHEN** the user requests to see the list
- **THEN** all persisted Todo items are returned containing their metadata (due date, priority, category)

#### Scenario: Complete a Todo
- **WHEN** a user marks a Todo as done
- **THEN** the Todo's status is updated to completed and persisted

#### Scenario: Delete a Todo
- **WHEN** a user deletes a Todo
- **THEN** the Todo item is removed from persistence

## ADDED Requirements
### Requirement: Natural Language Parsing
The system SHALL be able to interpret natural language strings to populate task attributes.

#### Scenario: Parse due date
- **WHEN** the input contains time-relative terms (e.g., "tomorrow", "next friday")
- **THEN** the `due_date` field is calculated and set

#### Scenario: Parse priority
- **WHEN** the input contains priority keywords (e.g., "!high", "priority:low")
- **THEN** the `priority` field is set accordingly

```

```markdown
## MODIFIED Requirements
### Requirement: Task Filtering
The UI SHALL provide comprehensive filtering capabilities for the task list.

#### Scenario: Filter by Status
- **WHEN** the user selects "Active", "Completed", or "All"
- **THEN** tasks matching the status are displayed

#### Scenario: Filter by Priority
- **WHEN** the user selects a specific priority (e.g., "High")
- **THEN** only tasks with that priority are displayed

#### Scenario: Filter by Category
- **WHEN** the user selects a category
- **THEN** only tasks belonging to that category are displayed

#### Scenario: Search
- **WHEN** the user types a search query
- **THEN** only tasks matching the query in title or description are displayed

### Requirement: Task Editing
The UI SHALL provide a mechanism to edit existing tasks' details.

#### Scenario: Edit Task Details
- **WHEN** the user chooses to edit a task
- **THEN** the form allows modifying title, description, due date, priority, and category
- **AND** saving the changes updates the persisted task

## ADDED Requirements
### Requirement: Quick Add
The UI SHALL provide a quick entry mechanism using natural language.

#### Scenario: Smart Entry
- **WHEN** the user types a command-like task (e.g., "Call mom tomorrow !high") into the Quick Add field
- **THEN** the task is created with the correct title ("Call mom"), due date (tomorrow's date), and priority (High)

```

I've created the change proposal `implement-optional-features` to address the optional requirements from the assessment.

**Proposal Summary:**
*   **Core:** Extend `Task` model with `due_date`, `priority`, and `category`. Add Natural Language Parsing (NLP) for smart task entry.
*   **UI:** Add sidebar filters (Search, Priority, Category), update task list to show new details, and enhance the "Add Task" form with a "Quick Add" (NLP) option.
*   **Docs:** Update `README.md` and `metadata.txt`.

**Files Created:**
*   `openspec/changes/implement-optional-features/proposal.md`
*   `openspec/changes/implement-optional-features/tasks.md`
*   `openspec/changes/implement-optional-features/design.md`
*   `openspec/changes/implement-optional-features/specs/core/spec.md` (Deltas)
*   `openspec/changes/implement-optional-features/specs/ui/spec.md` (Deltas)

The proposal has been validated and is ready for your review. If you approve, we can proceed with the implementation tasks.

---

**User**

1. for natural language input, you must use dateparser

2. Ignore migration trade-off right now, we dont have any data.



---

**Cursor**

```markdown
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


```

```markdown
## 1. Data Layer & Core Logic
- [ ] 1.1 Add `dateparser` to `pyproject.toml` and install dependencies.
- [ ] 1.2 Update `Task` model in `src/todo/models.py` to include `due_date`, `priority`, `category`.
- [ ] 1.3 Update database schema in `src/todo/db.py` (drop/recreate logic since no data).
- [ ] 1.4 Create `src/todo/nlp.py` using `dateparser` to extract dates and regex for priority/category.
- [ ] 1.5 Update repository in `src/todo/repository.py` to handle new fields.
- [ ] 1.6 Update tests in `tests/` to cover new fields and NLP logic.

## 2. User Interface
- [ ] 2.1 Update Sidebar in `src/todo/app.py` to include Search input, Category filter, and Priority filter.
- [ ] 2.2 Update Task List display to show Due Date, Priority badge, and Category.
- [ ] 2.3 Implement sorting logic (e.g., sort by Due Date, then Priority).
- [ ] 2.4 Update "Add Task" form to allow optional manual entry of new fields OR use the NLP input.
- [ ] 2.5 Add keyboard shortcut support (e.g., `Ctrl+Enter` to submit active form) if feasible in Streamlit.

## 3. Documentation
- [ ] 3.1 Update `README.md` to list new features.
- [ ] 3.2 Update `metadata.txt` to reflect implemented optional features.


```

```markdown
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


```

I have updated the proposal `implement-optional-features` to incorporate your feedback:

1.  **Natural Language Input**: Explicitly requires `dateparser`.
2.  **Migration**: Removed complexity; we will drop/recreate the DB schema as there is no production data.
3.  **Tasks**: Added `pyproject.toml` dependency update for `dateparser`.

The proposal passes validation. I'll wait for your confirmation to begin the implementation tasks.

---

**User**

/openspec-apply 

--- Cursor Command: openspec-apply.md ---
---
name: /openspec-apply
id: openspec-apply
category: OpenSpec
description: Implement an approved OpenSpec change and keep tasks in sync.
---
<!-- OPENSPEC:START -->
**Guardrails**
- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Refer to `openspec/AGENTS.md` (located inside the `openspec/` directory—run `ls openspec` or `openspec update` if you don't see it) if you need additional OpenSpec conventions or clarifications.

**Steps**
Track these steps as TODOs and complete them one by one.
1. Read `changes/<id>/proposal.md`, `design.md` (if present), and `tasks.md` to confirm scope and acceptance criteria.
2. Work through tasks sequentially, keeping edits minimal and focused on the requested change.
3. Confirm completion before updating statuses—make sure every item in `tasks.md` is finished.
4. Update the checklist after all work is done so each task is marked `- [x]` and reflects reality.
5. Reference `openspec list` or `openspec show <item>` when additional context is required.

**Reference**
- Use `openspec show <id> --json --deltas-only` if you need additional context from the proposal while implementing.
<!-- OPENSPEC:END -->

--- End Command ---

---

**Cursor**

```toml
[project]
name = "todo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Rubens", email = "38709237+andrader@users.noreply.github.com" }
]
requires-python = ">=3.13"
dependencies = [
    "dateparser>=1.2.0",
    "pydantic>=2.12.5",
    "streamlit>=1.52.1",
]

[project.scripts]
todo = "todo:main"

[build-system]
requires = ["uv_build>=0.9.11,<0.10.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "pytest>=9.0.2",
    "ruff>=0.14.8",
]

```

```python
import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the todo item")
    description: Optional[str] = Field(default=None, description="Detailed description")
    due_date: Optional[datetime] = Field(default=None, description="Due date for the task")
    priority: Priority = Field(default=Priority.MEDIUM, description="Task priority")
    category: Optional[str] = Field(default=None, description="Task category")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    priority: Optional[Priority] = None
    category: Optional[str] = None


class Todo(TodoBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True)

```

```python
import sqlite3
from contextlib import contextmanager

DB_NAME = "todo.db"


def init_db(db_path: str = DB_NAME):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Check if we need to migrate (simple drop/recreate strategy)
    try:
        c.execute("SELECT due_date FROM todos LIMIT 1")
    except sqlite3.OperationalError:
        # Column missing or table doesn't exist. 
        # For this assessment, we drop and recreate to handle the schema change.
        c.execute("DROP TABLE IF EXISTS todos")
        c.execute("""
            CREATE TABLE todos (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                due_date TIMESTAMP,
                priority TEXT DEFAULT 'Medium',
                category TEXT
            )
        """)
        
    conn.commit()
    conn.close()


@contextmanager
def get_db_connection(db_path: str = DB_NAME):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

```

```python
import re
from datetime import datetime
from typing import Optional, Dict, Any

from dateparser.search import search_dates  # type: ignore

from todo.models import Priority


def parse_task_input(text: str) -> Dict[str, Any]:
    """
    Parses a natural language string into task attributes.
    
    Expected format examples:
    - "Buy milk tomorrow !high #groceries"
    - "Call mom at 5pm"
    """
    
    # 1. Extract Priority
    priority = Priority.MEDIUM
    priority_map = {
        "!high": Priority.HIGH,
        "!medium": Priority.MEDIUM,
        "!low": Priority.LOW
    }
    
    # Check for priority markers
    for marker, p in priority_map.items():
        # Use regex to match whole words or end of string to avoid partial matches if needed,
        # but !high is distinct enough.
        if marker in text.lower():
            priority = p
            text = re.sub(re.escape(marker), "", text, flags=re.IGNORECASE)
            break
            
    # 2. Extract Category (#word)
    category = None
    # Match #word but ensure it's not part of another word if possible, but simple #\w+ is usually fine
    cat_match = re.search(r"#(\w+)", text)
    if cat_match:
        category = cat_match.group(1)
        text = re.sub(r"#\w+", "", text)
        
    # 3. Extract Date
    due_date = None
    # search_dates returns list of (substring, date_obj) or None
    try:
        dates = search_dates(text, settings={'PREFER_DATES_FROM': 'future', 'RETURN_AS_TIMEZONE_AWARE': False})
    except Exception:
        # dateparser might fail on some inputs
        dates = None
    
    if dates:
        # We assume the last date mentioned is the due date
        date_text, date_obj = dates[-1]
        due_date = date_obj
        # Remove the date text from the title
        # usage of replace might be dangerous if the date text appears elsewhere, but acceptable for this scope
        text = text.replace(date_text, "")
        
    # Clean up title
    title = re.sub(r"\s+", " ", text).strip()
    
    # If title became empty (e.g. input was just "tomorrow"), fallback?
    # For now, let Pydantic validation handle empty title if it occurs.
    
    return {
        "title": title,
        "priority": priority,
        "category": category,
        "due_date": due_date
    }

```

```python
from typing import List, Optional
from todo.models import Todo, TodoCreate, TodoUpdate
from todo.db import get_db_connection


class TodoRepository:
    def __init__(self, db_path: str = "todo.db"):
        self.db_path = db_path

    def _map_row_to_todo(self, row) -> Todo:
        return Todo(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            completed=bool(row["completed"]),
            created_at=row["created_at"],
            due_date=row["due_date"],
            priority=row["priority"],
            category=row["category"],
        )

    def add_todo(self, todo_create: TodoCreate) -> Todo:
        todo = Todo(**todo_create.model_dump())
        with get_db_connection(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO todos (id, title, description, completed, created_at, due_date, priority, category) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    todo.id,
                    todo.title,
                    todo.description,
                    todo.completed,
                    todo.created_at,
                    todo.due_date,
                    todo.priority.value,
                    todo.category,
                ),
            )
            conn.commit()
        return todo

    def get_todos(self) -> List[Todo]:
        with get_db_connection(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM todos")
            rows = cursor.fetchall()
            return [self._map_row_to_todo(row) for row in rows]

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        with get_db_connection(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
            row = cursor.fetchone()
            if row:
                return self._map_row_to_todo(row)
            return None

    def update_todo(self, todo_id: str, todo_update: TodoUpdate) -> Optional[Todo]:
        # First get existing
        existing = self.get_todo(todo_id)
        if not existing:
            return None

        update_data = todo_update.model_dump(exclude_unset=True)
        if not update_data:
            return existing

        # Update fields
        updated_todo = existing.model_copy(update=update_data)

        with get_db_connection(self.db_path) as conn:
            conn.execute(
                """
                UPDATE todos 
                SET title = ?, description = ?, completed = ?, due_date = ?, priority = ?, category = ? 
                WHERE id = ?
                """,
                (
                    updated_todo.title,
                    updated_todo.description,
                    updated_todo.completed,
                    updated_todo.due_date,
                    updated_todo.priority.value,
                    updated_todo.category,
                    todo_id,
                ),
            )
            conn.commit()

        return updated_todo

    def delete_todo(self, todo_id: str) -> bool:
        with get_db_connection(self.db_path) as conn:
            cursor = conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
            conn.commit()
            return cursor.rowcount > 0

```

```python
from datetime import datetime, timedelta
from todo.nlp import parse_task_input
from todo.models import Priority


def test_parse_simple_title():
    res = parse_task_input("Buy milk")
    assert res["title"] == "Buy milk"
    assert res["priority"] == Priority.MEDIUM
    assert res["category"] is None
    assert res["due_date"] is None


def test_parse_priority():
    res = parse_task_input("Buy milk !high")
    assert res["priority"] == Priority.HIGH
    assert res["title"] == "Buy milk"

    res = parse_task_input("Buy milk !low")
    assert res["priority"] == Priority.LOW


def test_parse_category():
    res = parse_task_input("Buy milk #personal")
    assert res["category"] == "personal"
    assert res["title"] == "Buy milk"


def test_parse_date():
    res = parse_task_input("Buy milk tomorrow")
    assert res["due_date"] is not None
    # We expect "tomorrow" to be roughly 24h from now or at least in future
    assert res["due_date"] > datetime.now()
    assert res["title"] == "Buy milk"


def test_parse_combined():
    res = parse_task_input("Buy milk tomorrow !high #groceries")
    assert res["priority"] == Priority.HIGH
    assert res["category"] == "groceries"
    assert res["due_date"] is not None
    assert res["title"] == "Buy milk"

```

```python
from datetime import datetime
from todo.models import TodoCreate, Todo, Priority
from pydantic import ValidationError
import pytest


def test_todo_create_valid():
    todo = TodoCreate(title="Buy milk")
    assert todo.title == "Buy milk"
    assert todo.description is None


def test_todo_create_with_optional_fields():
    dt = datetime(2025, 12, 25)
    todo = TodoCreate(title="Task", priority=Priority.HIGH, due_date=dt, category="Work")
    assert todo.priority == Priority.HIGH
    assert todo.due_date == dt
    assert todo.category == "Work"


def test_todo_create_invalid():
    with pytest.raises(ValidationError):
        TodoCreate(title="")


def test_todo_defaults():
    todo = Todo(title="Task")
    assert todo.id is not None
    assert todo.completed is False
    assert todo.created_at is not None
    assert todo.priority == Priority.MEDIUM
    assert todo.category is None
    assert todo.due_date is None

```

```python
import pytest
import os
from todo.repository import TodoRepository
from todo.models import TodoCreate, TodoUpdate, Priority
from todo.db import init_db

TEST_DB = "test_todo.db"


@pytest.fixture
def repo():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    init_db(TEST_DB)
    repository = TodoRepository(db_path=TEST_DB)
    yield repository
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_add_todo(repo):
    todo = repo.add_todo(TodoCreate(title="Test Task"))
    assert todo.id is not None
    assert todo.title == "Test Task"

    in_db = repo.get_todo(todo.id)
    assert in_db.id == todo.id
    assert in_db.title == "Test Task"
    assert in_db.priority == Priority.MEDIUM


def test_add_todo_with_fields(repo):
    todo = repo.add_todo(TodoCreate(title="Full Task", priority=Priority.LOW, category="Home"))
    assert todo.priority == Priority.LOW
    assert todo.category == "Home"
    
    in_db = repo.get_todo(todo.id)
    assert in_db.priority == Priority.LOW
    assert in_db.category == "Home"


def test_update_todo(repo):
    todo = repo.add_todo(TodoCreate(title="Original"))
    updated = repo.update_todo(todo.id, TodoUpdate(title="Updated", completed=True, priority=Priority.HIGH))

    assert updated.title == "Updated"
    assert updated.completed is True
    assert updated.priority == Priority.HIGH

    in_db = repo.get_todo(todo.id)
    assert in_db.title == "Updated"
    assert in_db.completed is True
    assert in_db.priority == Priority.HIGH


def test_delete_todo(repo):
    todo = repo.add_todo(TodoCreate(title="Delete Me"))
    assert repo.delete_todo(todo.id) is True
    assert repo.get_todo(todo.id) is None

```

```python
import streamlit as st
from datetime import datetime
from todo.repository import TodoRepository
from todo.db import init_db
from todo.models import TodoCreate, TodoUpdate, Priority
from todo.nlp import parse_task_input

st.set_page_config(page_title="Todo App", layout="centered")
st.title("Todo App")

# Initialize DB on first run
if "repo" not in st.session_state:
    init_db()
    st.session_state.repo = TodoRepository()

repo = st.session_state.repo

# --- Sidebar Filters ---
st.sidebar.header("Filters")
search_query = st.sidebar.text_input("Search", help="Search by title")
status_filter = st.sidebar.radio("Status", ["All", "Active", "Completed"], index=1)
priority_filter = st.sidebar.multiselect("Priority", [p.value for p in Priority])
category_filter = st.sidebar.text_input("Category", help="Filter by category name")

st.sidebar.divider()
st.sidebar.markdown("### Tips")
st.sidebar.info("Quick Add supports natural language!\n\nExample: 'Buy milk tomorrow !high #personal'")

# --- Add Todo ---
st.subheader("Add New Task")
add_tab1, add_tab2 = st.tabs(["Quick Add (NLP)", "Detailed Form"])

with add_tab1:
    with st.form("quick_add"):
        nlp_text = st.text_input("Describe your task...")
        submitted_quick = st.form_submit_button("Add Task")
        if submitted_quick and nlp_text:
            parsed = parse_task_input(nlp_text)
            if parsed["title"]:
                repo.add_todo(TodoCreate(
                    title=parsed["title"],
                    due_date=parsed["due_date"],
                    priority=parsed["priority"],
                    category=parsed["category"]
                ))
                st.success("Task added!")
                st.rerun()
            else:
                st.error("Could not extract a valid task title.")

with add_tab2:
    with st.form("detailed_add"):
        new_title = st.text_input("Title")
        new_desc = st.text_area("Description (optional)")
        col1, col2, col3 = st.columns(3)
        with col1:
            new_prio = st.selectbox("Priority", [p for p in Priority], format_func=lambda x: x.value, index=1) # Medium default
        with col2:
            new_cat = st.text_input("Category (optional)")
        with col3:
            new_due = st.date_input("Due Date", value=None)
            
        submitted_detail = st.form_submit_button("Add Task")
        if submitted_detail and new_title:
            # Convert date to datetime (start of day) if provided
            due_dt = None
            if new_due:
                due_dt = datetime.combine(new_due, datetime.min.time())
                
            repo.add_todo(TodoCreate(
                title=new_title, 
                description=new_desc if new_desc else None,
                priority=new_prio,
                category=new_cat if new_cat else None,
                due_date=due_dt
            ))
            st.success("Task added!")
            st.rerun()

st.divider()

# --- List Todos ---
todos = repo.get_todos()

# 1. Status Filter
if status_filter == "Active":
    todos = [t for t in todos if not t.completed]
elif status_filter == "Completed":
    todos = [t for t in todos if t.completed]

# 2. Search Filter
if search_query:
    todos = [t for t in todos if search_query.lower() in t.title.lower() or (t.description and search_query.lower() in t.description.lower())]

# 3. Priority Filter
if priority_filter:
    todos = [t for t in todos if t.priority.value in priority_filter]

# 4. Category Filter
if category_filter:
    todos = [t for t in todos if t.category and category_filter.lower() in t.category.lower()]

# Sorting
# Sort order: Active first, then Overdue/Soonest Due Date, then Priority (High>Med>Low)
prio_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}

def sort_key(t):
    # Tuple sorting:
    # 1. Completed (False < True) -> Active first
    # 2. Due Date (None is considered "far future" so tasks with dates appear first? Or last? 
    #    Let's put tasks with due dates first among active tasks.)
    #    Actually, `datetime.max` for None puts them last.
    due = t.due_date if t.due_date else datetime.max
    return (t.completed, due, prio_order[t.priority])

todos.sort(key=sort_key)

st.subheader(f"Tasks ({len(todos)})")

if not todos:
    st.info("No tasks found.")

for todo in todos:
    # Visual cues
    status_icon = "✅" if todo.completed else "⬜"
    
    # Priority Badge
    prio_icon = ""
    if todo.priority == Priority.HIGH:
        prio_icon = "🔴"
    elif todo.priority == Priority.MEDIUM:
        prio_icon = "🟡"
    elif todo.priority == Priority.LOW:
        prio_icon = "🔵"
        
    # Due Date Text
    due_str = ""
    if todo.due_date:
        # Check if overdue
        is_overdue = not todo.completed and todo.due_date < datetime.now()
        date_fmt = todo.due_date.strftime("%Y-%m-%d")
        if is_overdue:
            due_str = f"⚠️ Due: {date_fmt}"
        else:
            due_str = f"📅 {date_fmt}"
            
    cat_str = f"🏷️ {todo.category}" if todo.category else ""
    
    # Label construction
    label_parts = [status_icon, prio_icon, todo.title]
    if due_str:
        label_parts.append(f"[{due_str}]")
    if cat_str:
        label_parts.append(f"[{cat_str}]")
        
    expander_label = " ".join(part for part in label_parts if part)
    
    with st.expander(expander_label):
        with st.form(key=f"edit_form_{todo.id}"):
            # Edit fields
            col_a, col_b = st.columns([1, 3])
            with col_a:
                 e_completed = st.checkbox("Completed", value=todo.completed, key=f"chk_{todo.id}")
            with col_b:
                 e_title = st.text_input("Title", value=todo.title, key=f"tit_{todo.id}")
            
            e_desc = st.text_area("Description", value=todo.description or "", key=f"dsc_{todo.id}")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                e_prio = st.selectbox("Priority", [p for p in Priority], format_func=lambda x: x.value, index=[p for p in Priority].index(todo.priority), key=f"pri_{todo.id}")
            with c2:
                e_cat = st.text_input("Category", value=todo.category or "", key=f"cat_{todo.id}")
            with c3:
                # date_input needs date object, due_date is datetime
                default_date = todo.due_date.date() if todo.due_date else None
                e_due = st.date_input("Due Date", value=default_date, key=f"due_{todo.id}")

            update_btn = st.form_submit_button("Save Changes")
            
            if update_btn:
                new_due_dt = None
                if e_due:
                    new_due_dt = datetime.combine(e_due, datetime.min.time())
                
                repo.update_todo(
                    todo.id,
                    TodoUpdate(
                        title=e_title,
                        description=e_desc if e_desc else None,
                        completed=e_completed,
                        priority=e_prio,
                        category=e_cat if e_cat else None,
                        due_date=new_due_dt
                    )
                )
                st.success("Updated!")
                st.rerun()

        if st.button("Delete Task", key=f"del_{todo.id}", type="primary"):
            repo.delete_todo(todo.id)
            st.rerun()

```

```markdown
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

```

```plaintext
Time spent: ~90 minutes (Original ~60 + Extended Features)
AI tools used: Cursor (Agent mode with gemini-3-pro-preview + OpenSpec framework)
Features implemented:
- Create tasks (Title, Description)
- List tasks
- Complete/Uncomplete tasks
- Edit tasks
- Delete tasks
- Persistence (SQLite)
- Filtering (All, Active, Completed)
- CI/CD (GitHub Actions)
- Unit Tests
- Due dates / reminders
- Priority levels
- Search
- Categories
- Natural language input ("Quick Add")
Features not implemented:
- Keyboard shortcuts (Partial support via standard form submission)
- Drag-and-drop reordering
Time constraints: Extended to implement optional "nice-to-have" features.
Out of scope: Authentication, Remote Database, Multi-user support.
Potential future improvements: Add a calendar view; add drag-and-drop reordering; push notifications for overdue tasks.

```

```markdown
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

```

I have successfully implemented all optional features outlined in the proposal.

**Implementation Summary:**
1.  **Backend:**
    *   Updated `Task` model with `due_date`, `priority`, and `category`.
    *   Updated `db.py` to handle schema changes (drop/recreate strategy used).
    *   Implemented NLP parsing in `nlp.py` using `dateparser` and regex.
    *   Updated `TodoRepository` to handle the new fields.
    *   Added comprehensive tests covering NLP, Models, and DB operations.
2.  **Frontend (UI):**
    *   Added **Quick Add** tab supporting natural language input (e.g., "Buy milk tomorrow !high #groceries").
    *   Added **Sidebar Filters** for Status, Search, Priority, and Category.
    *   Enhanced **Task List** with visual badges for Priority and Due Date.
    *   Implemented **Sorting**: Active > Due Soon > Priority.
    *   Updated **Edit Form** to support all new fields.
3.  **Documentation:**
    *   Updated `README.md` with new features and setup instructions.
    *   Updated `metadata.txt`.

**Verification:**
*   `uv run pytest` passed successfully (13 tests passed).
*   `openspec archive` completed successfully.

You can run the app with:
```bash
uv run streamlit run src/todo/app.py
```

```shellscript
uv run streamlit run src/todo/app.py
```

