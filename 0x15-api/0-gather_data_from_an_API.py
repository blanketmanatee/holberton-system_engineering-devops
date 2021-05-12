#!/usr/bin/python3
import json
import requests
from sys import argv
""" use rest api for given employee id returning information about their todo list progress """


if __name__ == "__main__":
    """
    gets list progress
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users"
                        ).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos"
                        ).json()
    done = []
    for done in todo:
        if done.get('completed') is True:
            done.append(done.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(done), len(todo)))
    for task in done:
        print("\t {}".format(task))
