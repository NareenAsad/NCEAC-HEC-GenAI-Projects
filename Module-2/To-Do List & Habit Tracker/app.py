import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# ---------- File Setup ----------
TODO_FILE = "todos.json"
HABIT_FILE = "habits.json"

# ---------- Utility Functions ----------
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# ---------- To-Do List ----------
def todo_section():
    st.header("To-Do List")
    todos = load_data(TODO_FILE)

    new_task = st.text_input("Add a new task")
    if st.button("Add Task") and new_task:
        todos[new_task] = {"completed": False}
        save_data(TODO_FILE, todos)
        st.success("Task added!")

    if todos:
        for task, info in list(todos.items()):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(task)
            with col2:
                if st.checkbox("Done", value=info["completed"], key=task):
                    todos[task]["completed"] = True
                else:
                    todos[task]["completed"] = False
            with col3:
                if st.button("Delete", key=f"del_{task}"):
                    del todos[task]
                    save_data(TODO_FILE, todos)
                    st.experimental_rerun()
        save_data(TODO_FILE, todos)
    else:
        st.info("No tasks yet. Add one above!")

# ---------- Habit Tracker ----------
def habit_section():
    st.header("Habit Tracker")
    habits = load_data(HABIT_FILE)

    new_habit = st.text_input("Add a new habit")
    if st.button("Add Habit") and new_habit:
        if new_habit not in habits:
            habits[new_habit] = {"streak": 0, "dates": []}
            save_data(HABIT_FILE, habits)
            st.success("Habit added!")

    today = str(date.today())
    for habit, data in habits.items():
        done_today = today in data["dates"]
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(habit)
        with col2:
            if st.button("Done Today" if not done_today else "Undo", key=habit):
                if done_today:
                    data["dates"].remove(today)
                    data["streak"] = max(0, data["streak"] - 1)
                else:
                    data["dates"].append(today)
                    data["streak"] += 1
                save_data(HABIT_FILE, habits)
                st.rerun()
        with col3:
            st.write(f"{data['streak']} days")

    if habits:
        st.subheader("Streak Progress")
        df = pd.DataFrame(
            {"Habit": [h for h in habits],
             "Streak": [habits[h]["streak"] for h in habits]}
        )
        st.bar_chart(df.set_index("Habit"))

# ---------- Main App ----------
def main():
    st.set_page_config(page_title="To-Do & Habit Tracker", page_icon="✅", layout="centered")
    st.title("To-Do List & Habit Tracker")

    menu = ["To-Do List", "Habit Tracker", "About"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "To-Do List":
        todo_section()
    elif choice == "Habit Tracker":
        habit_section()
    else:
        st.header("About")
        st.markdown("""
        This is a simple **To-Do List & Habit Tracker** built with **Streamlit**.  
        You can:
        - Add, complete, or delete tasks.  
        - Track daily habits and view your streak progress.  
        - Your data is saved locally (JSON files).  
        """)

if __name__ == "__main__":
    main()
