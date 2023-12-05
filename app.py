
import streamlit as st
import requests

# Define API endpoints
BASE_URL = "https://frontendtodo-qypza5jeea-uc.a.run.app"  
ADD_TASK_ENDPOINT = "/addtask"
DELETE_ALL_TASK_ENDPOINT = "/deletealltask"
GET_ALL_TASKS_ENDPOINT = "/tasks"

# Streamlit app
def main():
    st.title("Todo List App")

    # Input field for adding a new task
    new_task = st.text_input("Add a new task:")

    # Button to add a new task
    if st.button("Add Task"):
        add_task(new_task)

    # Display the current tasks
    display_tasks()

# Function to add a new task
def add_task(task):
    try:
        response = requests.post(BASE_URL + ADD_TASK_ENDPOINT, json={"task": task})
        response.raise_for_status()
        st.success(f"Task '{task}' added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding task: {e}")

# Function to display the current tasks
def display_tasks():
    try:
        response = requests.get(BASE_URL + GET_ALL_TASKS_ENDPOINT)
        response.raise_for_status()
        tasks = response.json()

        # Display tasks
        if tasks:
            st.subheader("Current Tasks:")
            for task in tasks:
                st.write(f"- {task.get('task')}")
        else:
            st.info("No tasks available.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching tasks: {e}")

if __name__ == "__main__":
    main()

