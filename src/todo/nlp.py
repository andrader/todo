import re
from typing import Any, Dict

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
        "!low": Priority.LOW,
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
        dates = search_dates(
            text,
            settings={"PREFER_DATES_FROM": "future", "RETURN_AS_TIMEZONE_AWARE": False},
        )
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
        "due_date": due_date,
    }
