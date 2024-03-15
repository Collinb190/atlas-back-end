#!/usr/bin/python3
"""
For a given employee ID, return information about their todo list progress.
"""
import json
import requests
import sys


def get_user_name(user_id):
    """ Get the users name. """
    responce = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    if responce.status_code == 200:
        return responce.json().get('username', 'Unknown')
    else:
        return 'Unknown'


def export_to_json(employee_id, todos):
    """ Exports todos to json format. """
    user_name = get_user_name(employee_id)
    user_data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user_name
            }
            for todo in todos
        ]
    }
    file_name = f"{employee_id}.json"
    with open(file_name, mode='w') as f:
        json.dump(user_data, f, indent=2)


def todo_progress(employee_id):
    """ Displays the todo list progress. """
    responce = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    if responce.status_code != 200:
        print(f"Failed to get data for employee ID: {employee_id}")
        return
    todos = responce.json()
    export_to_json(employee_id, todos)

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed = len(completed_tasks)
    total_tasks = len(todos)
    employee_name = get_user_name(employee_id)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    todo_progress(employee_id)
