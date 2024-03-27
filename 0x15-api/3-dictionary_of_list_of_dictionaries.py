#!/usr/bin/python3
'''
i dont even know anymore
'''

if __name__ == '__main__':
    import json
    import requests

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    json_return = {}
    username_dict = {}

    for user in users:
        uid = user.get('id')
        json_return[uid] = []
        username_dict[uid] = user.get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for item in todos:
        json_dictionary = {}
        uid = item.get('userId')
        json_dictionary['task'] = item.get('title')
        json_dictionary['username'] = username_dict.get(uid)
        json_dictionary['completed'] = item.get('completed')
        json_return.get(uid).append(json_dictionary)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_return, json_file)
