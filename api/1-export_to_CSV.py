#!/usr/bin/python3
"""
For a given employee ID, return information about their todo list progress.
"""
import csv
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


def export_to_csv(employee_id, todos):
    """ Exports todos to CSV format. """
    user_name = get_user_name(employee_id)
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [employee_id, user_name, todo['completed'], todo['title']]
            )


def todo_progress(employee_id):
    """ Displays the todo list progress. """
    responce = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    if responce.status_code != 200:
        print(f"Failed to get data for employee ID: {employee_id}")
        return
    todos = responce.json()
    export_to_csv(employee_id, todos)

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
