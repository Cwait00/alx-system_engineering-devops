#!/usr/bin/python3

import requests
import csv
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

def export_to_csv(employee_id, employee_name, todos):
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
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
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

    export_to_csv(employee_id, employee_name, todos)
