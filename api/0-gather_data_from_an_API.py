#!/usr/bin/python3
"""
For a given employee ID, return information about their todo list progress.
"""
import requests
import sys


def get_user_name(user_id):
    """ Get the users name. """
    responce = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    if responce.status_code == 200:
        return responce.json().get('name', 'Unknown')
    else:
        return 'Unknown'

def todo_progress(employee_id):
    """ Displays the todo list progress. """
    responce = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    if responce.status_code != 200:
        print(f"Failed to get data for employee ID: {employee_id}")
        return
    todos = responce.json()
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed = len(completed_tasks)
    total_tasks = len(todos)
    employee_name = get_user_name(employee_id)

    # print the employees todo list progress.
    print(f"Employee {employee_name} is done with tasks ({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    todo_progress(employee_id)
