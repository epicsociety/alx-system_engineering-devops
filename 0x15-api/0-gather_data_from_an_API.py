#!/usr/bin/python3
"""
use the REST API to retrive info about employee
"""

import requests
import sys
import urllib3

# Disable the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_employee_todo_progress(employee_id):
    """ get employee todo list, get completed tasks
    Args (int):
        employee_id
    Returns: string
    """

    employees = requests.get("https://jsonplaceholder.typicode.com/users/",
                             verify=False).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(employee_id), verify=False).json()

    for employee in employees:
        if employee.get('id') == employee_id:
            employee_name = employee.get("name")
            break

    completed_tasks = []
    for todo in todos:
        if todo.get('completed'):
            completed_tasks.append(todo.get('title'))

    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
