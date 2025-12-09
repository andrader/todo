from todo.models import TodoCreate, Todo
from pydantic import ValidationError
import pytest


def test_todo_create_valid():
    todo = TodoCreate(title="Buy milk")
    assert todo.title == "Buy milk"
    assert todo.description is None


def test_todo_create_invalid():
    with pytest.raises(ValidationError):
        TodoCreate(title="")


def test_todo_defaults():
    todo = Todo(title="Task")
    assert todo.id is not None
    assert todo.completed is False
    assert todo.created_at is not None
