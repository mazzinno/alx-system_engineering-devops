#!/usr/bin/python3
'''getting data from RESTapi'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    # fetch data
    response = requests.get(url)
    # parse data
    userdata = response.json()
    # name
    EMPLOYEE_NAME = userdata.get('name')

    all_todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        sys.argv[1])
    # the fetch data
    all_todos_response = requests.get(all_todos_url)
    # the parsing data
    all_todos_data = all_todos_response.json()
    # the TOTAL_NUMBER_OF_TASKS
    TOTAL_NUMBER_OF_TASKS = len(all_todos_data)

    todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        sys.argv[1] +
        '&completed=true')

    TASK_TITLE = []
    # now we start to fetch data
    todos_response = requests.get(todos_url)
    # now we start to parse data
    todos_data = todos_response.json()
    for todo in todos_data:
        TASK_TITLE.append(todo.get('title'))
    # NUMBER_OF_DONE_TASKS
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)

    # printing the resaults
    print(f'Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for todo in TASK_TITLE:
        print(f'\t {todo}')
