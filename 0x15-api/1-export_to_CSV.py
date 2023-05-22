#!/usr/bin/python3
"""
use the REST API to retrive info about employee and write on a file
"""

import csv
import requests
import sys
import urllib3

# Disable the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_employee_and_tasks(userId):
    """ get employee todo list, get all tasks and write on a file
    Args (int):
        userId
    Returns: file
    """

    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                 .format(userId), verify=False).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userId), verify=False).json()

    with open("{}.csv".format(userId), 'w') as acsvfile:
        csvwriter = csv.writer(acsvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csvwriter.writerow([userId, employee_name.get('username'),
                                task.get('completed'), task.get('title')])

if __name__ == '__main__':
    userId = int(sys.argv[1])
    get_employee_and_tasks(userId)
