#!/usr/bin/python3
"""
Script to gather data from an API and export the data to JSON format.

"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # API endpoint URL
    url = 'https://jsonplaceholder.typicode.com/todos'

    # Make GET request to the API
    response = requests.get(url)

    # Convert response to JSON format
    data = response.json()

    # Dictionary to store tasks for each user
    user_tasks = {}

    # Populate user_tasks dictionary
    for task in data:
        user_id = task.get('userId')
        task_data = {
            "username": "",
            "task": task.get('title'),
            "completed": task.get('completed')
        }
        if user_id in user_tasks:
            user_tasks[user_id].append(task_data)
        else:
            user_tasks[user_id] = [task_data]

    # Get user names from another endpoint (assuming user id matches)
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Populate usernames in user_tasks dictionary
    for user in users_data:
        user_id = user.get('id')
        if user_id in user_tasks:
            for task_data in user_tasks[user_id]:
                task_data['username'] = user.get('username')

    # Export data to JSON format
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)
