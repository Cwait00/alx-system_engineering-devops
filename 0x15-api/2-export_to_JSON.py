#!/usr/bin/python3

import requests
import json
import sys

def gather_data_from_api(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    todos = response.json()
    return todos

def get_employee_name(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    employee_info = response.json()
    return employee_info.get('name')  # Extract employee name

def export_to_json(employee_id, employee_name, todos):
    filename = f"{employee_id}.json"
    data = {employee_id: []}
    for todo in todos:
        data[employee_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        })

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    todos = gather_data_from_api(employee_id)
    if not todos:
        print("No tasks found for the employee.")
        sys.exit(1)

    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print("Failed to retrieve employee name.")
        sys.exit(1)

    export_to_json(employee_id, employee_name, todos)
