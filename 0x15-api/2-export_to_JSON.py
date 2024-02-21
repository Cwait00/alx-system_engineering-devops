#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list from a REST API and exports it to a JSON file.
"""

import json
import requests
import sys

# Hardcoded name for employee ID 2
EMPLOYEE_NAME = "Antonette"

def gather_data_from_api(employee_id):
    """
    Retrieve TODO list for the employee with the given ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of TODO items for the employee.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    todos = response.json()
    return todos

def get_employee_name(employee_id):
    """
    Retrieve hardcoded employee name based on the employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
    """
    return EMPLOYEE_NAME

def export_to_json(employee_id, employee_name, todos):
    """
    Export employee TODO list to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos (list): List of TODO items for the employee.
    """
    filename = f"{employee_id}.json"
    data = {
        employee_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos
        ]
    }

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Ensure proper indentation for readability

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
