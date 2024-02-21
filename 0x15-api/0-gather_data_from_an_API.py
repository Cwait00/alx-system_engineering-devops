#!/usr/bin/python3

import requests
import sys

def get_employee_name(employee_id):
    """
    Retrieve the name of the employee with the given ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee, or None if not found.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    employee_info = response.json()
    return employee_info.get('name')  # Corrected to handle missing name gracefully

def gather_data_from_api(employee_id):
    """
    Gather data from the API for the employee with the given ID and print it.

    Args:
        employee_id (int): The ID of the employee.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Retrieve employee name
    employee_name = get_employee_name(employee_id)
    if employee_name is None:
        print(f"Error: Unable to retrieve employee name for ID {employee_id}")
        return

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")  # Print only completed tasks with correct formatting

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    gather_data_from_api(employee_id)
