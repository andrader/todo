from typing import List, Optional
from todo.models import Todo, TodoCreate, TodoUpdate
from todo.db import get_db_connection


class TodoRepository:
    def __init__(self, db_path: str = "todo.db"):
        self.db_path = db_path

    def add_todo(self, todo_create: TodoCreate) -> Todo:
        todo = Todo(**todo_create.model_dump())
        with get_db_connection(self.db_path) as conn:
            conn.execute(
                "INSERT INTO todos (id, title, description, completed, created_at) VALUES (?, ?, ?, ?, ?)",
                (
                    todo.id,
                    todo.title,
                    todo.description,
                    todo.completed,
                    todo.created_at,
                ),
            )
            conn.commit()
        return todo

    def get_todos(self) -> List[Todo]:
        with get_db_connection(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM todos")
            rows = cursor.fetchall()
            return [
                Todo(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    completed=bool(row["completed"]),
                    created_at=row["created_at"],
                )
                for row in rows
            ]

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        with get_db_connection(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
            row = cursor.fetchone()
            if row:
                return Todo(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    completed=bool(row["completed"]),
                    created_at=row["created_at"],
                )
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
                "UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?",
                (
                    updated_todo.title,
                    updated_todo.description,
                    updated_todo.completed,
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
