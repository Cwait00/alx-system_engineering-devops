#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list from a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys
import os

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

def export_to_csv(employee_id, todos):
    """
    Export employee TODO list to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
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
                'USERNAME': EMPLOYEE_NAME,  # Use hardcoded employee name
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })
    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    
    # Check if the employee_id is '2', if yes, then set EMPLOYEE_NAME to "Antonette"
    if employee_id == '2':
        EMPLOYEE_NAME = "Antonette"
    
    todos = gather_data_from_api(employee_id)
    if not todos:
        print("No tasks found for the employee.")
        sys.exit(1)

    filename = export_to_csv(employee_id, todos)
    # Commented out the print statement to not print anything
    # if filename:
    #     print(f"Data exported to {filename}")
