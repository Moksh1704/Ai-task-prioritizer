import streamlit as st
from ai_utils import ask_ai_for_priority

st.title("AI Task Prioritizer")

st.write("Enter tasks one by one. Click the button to see priority.")

task = st.text_input("Enter a task")

if st.button("Get Priority"):
    if task.strip() == "":
        st.warning("Please enter a task")
    else:
        priority = ask_ai_for_priority(task)
        st.success(f"Priority: {priority}")
