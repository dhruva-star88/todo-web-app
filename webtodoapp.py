import streamlit as st
import funcweb

todos = funcweb.get_todos()


def add_todo():
    user_given_todo = st.session_state["new_todo"] + "\n"
    todos.append(user_given_todo)
    funcweb.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my todo App")
st.write("This app increases your productivity..")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        funcweb.write_todos(todos)
        del st.session_state[todo]  # updates in the session_state
        st.experimental_rerun()

st.text_input(label="Enter a Todo", placeholder="Add a New Todo...",
              on_change=add_todo, key="new_todo")

st.session_state
print("Hello")
