from datetime import datetime
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

