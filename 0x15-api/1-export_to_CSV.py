#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list from a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys
import os

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

def get_employee_info(employee_id):
    """
    Retrieve employee information from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee ID and name.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return None, None

    employee_info = response.json()
    return employee_info.get('id'), employee_info.get('name')  # Extract employee ID and name

def export_to_csv(employee_id, employee_name, todos):
    """
    Export employee TODO list to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos (list): List of TODO items for the employee.
    """
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })
    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    todos = gather_data_from_api(employee_id)
    if not todos:
        print("No tasks found for the employee.")
        sys.exit(1)

    employee_id, employee_name = get_employee_info(employee_id)
    if not employee_id or not employee_name:
        print("Failed to retrieve employee information.")
        sys.exit(1)

    filename = export_to_csv(employee_id, employee_name, todos)
    if filename:
        print(f"Data exported to {filename}")
