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


def export_to_json(all_data):
    """ Exports todos to json format. """
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as f:
        json.dump(all_data, f, indent=2)


def todo_progress_all():
    """ Displays the todo list progress. """
    all_data = {}
    for employee_id in range(1, 11):
        responce = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        if responce.status_code == 200:
            todos = responce.json()
            user_name = get_user_name(employee_id)
            user_data = [
                {
                    "username": user_name,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in todos
            ]
            all_data[str(employee_id)] = user_data
        else:
            print(f"Failed to get data for employee ID: {employee_id}")

    export_to_json(all_data)

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed = len(completed_tasks)
    total_tasks = len(todos)
    employee_name = get_user_name(employee_id)


if __name__ == '__main__':
    todo_progress_all()
