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
    todo = repo.add_todo(
        TodoCreate(title="Full Task", priority=Priority.LOW, category="Home")
    )
    assert todo.priority == Priority.LOW
    assert todo.category == "Home"

    in_db = repo.get_todo(todo.id)
    assert in_db.priority == Priority.LOW
    assert in_db.category == "Home"


def test_update_todo(repo):
    todo = repo.add_todo(TodoCreate(title="Original"))
    updated = repo.update_todo(
        todo.id, TodoUpdate(title="Updated", completed=True, priority=Priority.HIGH)
    )

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
