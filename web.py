import streamlit as st

import functions
def add_todo():
    temp = st.session_state['add']
    temp=temp+"\n"
    todos=functions.get_todos("todos.txt")
    todos.append(temp)
    functions.write_todos(todos)

st.title("Welcome to my to-do apps")
st.text("this apps will increase your productivity")
todos=functions.get_todos("todos.txt")
for index,task in enumerate(todos):
    check_list = st.checkbox(task, key=task)
    if check_list:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[task]


st.text_input(label="",placeholder="Add new text....", on_change=add_todo, key='add')