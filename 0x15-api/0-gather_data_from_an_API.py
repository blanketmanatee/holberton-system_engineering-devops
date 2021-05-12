#!/usr/bin/python3
""" use API for employee progress on Todo list """
import json
import requests
import sys


if __name__ == "__main__":
    """
    gets list progress
    """
    user = requests.get("https://jsonplaceholder.typicode.com/users"
                        ).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos"
                        ).json()
    done = []
    employee = [i for i in user if i.get('id') == int(sys.argv[1])][0]
    task = [i for i in todo if i.get('userId') == int(sys.argv[1])]
    done = [i for i in task if i.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".
          format(employee.get('name'), len(done), len(task)))
    for task in done:
        print("\t {}".format(task.get("title")))
