#!/usr/bin/python3
""" use the REST API to retrive info abou employee """

import sys
import requests


def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    completed_tasks = []
    for todo in todos:
        if todo.get('completed'):
            completed_tasks.append(todo.get('title'))

    employee_name = None
    for todo in todos:
        if todo.get('userId') == employee_id:
            employee_name = todo.get('username')
            break

    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
