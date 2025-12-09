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
st.sidebar.info(
    "Quick Add supports natural language!\n\nExample: 'Buy milk tomorrow !high #personal'"
)

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
                repo.add_todo(
                    TodoCreate(
                        title=parsed["title"],
                        due_date=parsed["due_date"],
                        priority=parsed["priority"],
                        category=parsed["category"],
                    )
                )
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
            new_prio = st.selectbox(
                "Priority",
                [p for p in Priority],
                format_func=lambda x: x.value,
                index=1,
            )  # Medium default
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

            repo.add_todo(
                TodoCreate(
                    title=new_title,
                    description=new_desc if new_desc else None,
                    priority=new_prio,
                    category=new_cat if new_cat else None,
                    due_date=due_dt,
                )
            )
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
    todos = [
        t
        for t in todos
        if search_query.lower() in t.title.lower()
        or (t.description and search_query.lower() in t.description.lower())
    ]

# 3. Priority Filter
if priority_filter:
    todos = [t for t in todos if t.priority.value in priority_filter]

# 4. Category Filter
if category_filter:
    todos = [
        t for t in todos if t.category and category_filter.lower() in t.category.lower()
    ]

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
                e_completed = st.checkbox(
                    "Completed", value=todo.completed, key=f"chk_{todo.id}"
                )
            with col_b:
                e_title = st.text_input("Title", value=todo.title, key=f"tit_{todo.id}")

            e_desc = st.text_area(
                "Description", value=todo.description or "", key=f"dsc_{todo.id}"
            )

            c1, c2, c3 = st.columns(3)
            with c1:
                e_prio = st.selectbox(
                    "Priority",
                    [p for p in Priority],
                    format_func=lambda x: x.value,
                    index=[p for p in Priority].index(todo.priority),
                    key=f"pri_{todo.id}",
                )
            with c2:
                e_cat = st.text_input(
                    "Category", value=todo.category or "", key=f"cat_{todo.id}"
                )
            with c3:
                # date_input needs date object, due_date is datetime
                default_date = todo.due_date.date() if todo.due_date else None
                e_due = st.date_input(
                    "Due Date", value=default_date, key=f"due_{todo.id}"
                )

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
                        due_date=new_due_dt,
                    ),
                )
                st.success("Updated!")
                st.rerun()

        if st.button("Delete Task", key=f"del_{todo.id}", type="primary"):
            repo.delete_todo(todo.id)
            st.rerun()
