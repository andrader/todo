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
