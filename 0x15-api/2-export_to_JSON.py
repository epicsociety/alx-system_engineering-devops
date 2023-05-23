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


def employee_info_to_json(userId):
    """ get employee todo list, get all tasks and write on a file
    Args (int)
        userId
    Returns: file
    """

    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId), verify=False).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userId), verify=False).json()

    todolist = []
    for todo in todos:
        mydict = {}
        mydict['task'] = todo.get("title")
        mydict['completed'] = todo.get("completed")
        mydict['username'] = employee.get("username")
        todolist.append(mydict)

    json_obj = {}
    json_obj[userId] = todolist

    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)


if __name__ == '__main__':
    userId = int(sys.argv[1])
    employee_info_to_json(userId)
