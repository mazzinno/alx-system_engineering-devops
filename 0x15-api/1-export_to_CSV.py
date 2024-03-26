#!/usr/bin/python3
'''
For a given employee ID
it returns information about his
TODO list progress in CSV format.
'''

if __name__ == '__main__':
    import csv
    import requests
    import sys

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    USER_ID = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(USER_ID))
    name = user.json()

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(USER_ID))
    todos = req.json()

    with open(USER_ID + '.csv', 'w', newline='') as csv_file:
        write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for item in todos:
            write.writerow([name['id'], name['username'],
                            item['completed'], item['title']])
