#!/usr/bin/python3

import requests
import sys

def get_employee_name(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    employee_info = response.json()
    return employee_info['name']

def gather_data_from_api(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return

    todos = response.json()
    employee_name = get_employee_name(employee_id)
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    completed_task_titles = [todo['title'] for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
