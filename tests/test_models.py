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
