#!/usr/bin/python3
"""
Scipt use the REST API to retrive info about employee and write on a json file
"""

import csv
import json
import requests
import sys
import urllib3

# Disable the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def employee_info_to_json():
    """ get employee todo list, get all tasks and write on a file
    Args (int)
        userId
    Returns: file
    """

    employees = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    dict_Id = {}
    dict_users = {}

    for employee in employees:
        emp_id = employee.get("id")
        dict_Id[emp_id] = []
        dict_users[emp_id] = employee.get('username')

    for todo in todos:
        mydict = {}
        emp_id = todo.get('userId')
        mydict['username'] = dict_users[emp_id]
        mydict['tasks'] = todo.get("title")
        mydict['completed'] = todo.get("completed")
        dict_Id.get(emp_id).append(mydict)

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dict_Id, jsonfile)


if __name__ == '__main__':
    employee_info_to_json()
