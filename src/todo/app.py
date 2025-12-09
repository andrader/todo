import streamlit as st
from todo.repository import TodoRepository
from todo.db import init_db
from todo.models import TodoCreate, TodoUpdate

st.title("Todo App")

# Initialize DB on first run
if "repo" not in st.session_state:
    init_db()
    st.session_state.repo = TodoRepository()

repo = st.session_state.repo

# Add Todo
with st.form("add_todo"):
    new_title = st.text_input("New Task")
    submitted = st.form_submit_button("Add")
    if submitted and new_title:
        repo.add_todo(TodoCreate(title=new_title))
        st.success("Added!")
        st.rerun()

# List Todos
todos = repo.get_todos()
for todo in todos:
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
    with col1:
        done = st.checkbox("", value=todo.completed, key=f"check_{todo.id}")
        if done != todo.completed:
            repo.update_todo(todo.id, TodoUpdate(completed=done))
            st.rerun()
    with col2:
        st.write(todo.title)
    with col3:
        if st.button("Delete", key=f"del_{todo.id}"):
            repo.delete_todo(todo.id)
            st.rerun()
