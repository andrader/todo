import streamlit as st
from todo.repository import TodoRepository
from todo.db import init_db
from todo.models import TodoCreate, TodoUpdate

st.set_page_config(page_title="Todo App", layout="centered")
st.title("Todo App")

# Initialize DB on first run
if "repo" not in st.session_state:
    init_db()
    st.session_state.repo = TodoRepository()

repo = st.session_state.repo

# --- Sidebar / Top Actions ---

# Filter
filter_option = st.radio(
    "Filter Tasks:",
    ["All", "Active", "Completed"],
    horizontal=True
)

st.divider()

# --- Add Todo ---
st.subheader("Add New Task")
with st.form("add_todo"):
    new_title = st.text_input("Title")
    new_desc = st.text_area("Description (optional)")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_title:
        repo.add_todo(TodoCreate(title=new_title, description=new_desc if new_desc else None))
        st.success("Task added!")
        st.rerun()

st.divider()

# --- List Todos ---
todos = repo.get_todos()

# Apply Filter
if filter_option == "Active":
    todos = [t for t in todos if not t.completed]
elif filter_option == "Completed":
    todos = [t for t in todos if t.completed]

st.subheader(f"Tasks ({len(todos)})")

if not todos:
    st.info("No tasks found.")

for todo in todos:
    # Use an expander for each task to keep the main list clean
    # The label includes the status icon and title
    status_icon = "✅" if todo.completed else "⬜"
    expander_label = f"{status_icon} {todo.title}"
    
    with st.expander(expander_label):
        # Edit Form inside the expander
        with st.form(key=f"edit_form_{todo.id}"):
            # Completion Status
            is_completed = st.checkbox("Completed", value=todo.completed, key=f"check_{todo.id}")
            
            # Editable Fields
            edit_title = st.text_input("Title", value=todo.title, key=f"title_{todo.id}")
            edit_desc = st.text_area("Description", value=todo.description or "", key=f"desc_{todo.id}")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                update_submitted = st.form_submit_button("Update Task")
            with col2:
                # We can't put a button inside a form that isn't a submit button easily if we want specific logic
                # So we make Delete a separate button outside or handle it carefully.
                # Actually, standard Streamlit forms only have one submit. 
                # Let's put Delete OUTSIDE the form but inside the expander.
                pass
        
        if update_submitted:
            repo.update_todo(
                todo.id, 
                TodoUpdate(
                    title=edit_title, 
                    description=edit_desc if edit_desc else None, 
                    completed=is_completed
                )
            )
            st.success("Updated!")
            st.rerun()

        # Delete Button (Outside form to avoid form submission confusion)
        if st.button("Delete Task", key=f"del_{todo.id}", type="primary"):
            repo.delete_todo(todo.id)
            st.rerun()
