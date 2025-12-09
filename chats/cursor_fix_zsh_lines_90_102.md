# Fix Zsh lines 90-102
_Exported on 12/8/2025 at 23:22:51 GMT-3 from Cursor (2.1.50)_

---

**User**

fix @zsh (90-102) 

---

**Cursor**

```python
import sqlite3
from contextlib import contextmanager
from datetime import datetime

# Register adapter for datetime to avoid DeprecationWarning in Python 3.12+
def adapt_datetime(dt):
    return dt.isoformat(" ")

sqlite3.register_adapter(datetime, adapt_datetime)

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

The DeprecationWarning from `sqlite3` regarding the default datetime adapter has been fixed.

I added a custom datetime adapter registration in `src/todo/db.py` to explicitly handle `datetime` objects by converting them to ISO format strings with a space separator (matching the previous default behavior but without the warning).

```python:src/todo/db.py
# ...
from datetime import datetime

# Register adapter for datetime to avoid DeprecationWarning in Python 3.12+
def adapt_datetime(dt):
    return dt.isoformat(" ")

sqlite3.register_adapter(datetime, adapt_datetime)
# ...
```

I verified the fix by running the tests (`tests/test_db.py`) and confirming that no warnings are emitted and all tests pass. I also ran the full test suite to ensure no regressions.

```python
# ...
from datetime import datetime

# Register adapter for datetime to avoid DeprecationWarning in Python 3.12+
def adapt_datetime(dt):
    return dt.isoformat(" ")

sqlite3.register_adapter(datetime, adapt_datetime)
# ...
```

