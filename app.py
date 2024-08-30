import argparse
import json
import os

tFile = "tasks.json"

def create_file():
    """Create a new JSON file with an empty list of tasks."""
    with open(tFile, 'w') as file:
        json.dump([], file)
    return []

def load_tasks():
    """Load tasks from the JSON file. Create the file if it doesn't exist."""
    if not os.path.exists(tFile):
        return create_file()
    with open(tFile, 'r') as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(tFile, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(name, status="Not Started"):
    """Add a new task with the specified name and status."""
    if status not in ["Not Started", "Progressing", "Done"]:
        print("Error: Invalid status. Must be 'Not Started', 'Progressing', or 'Done'.")
        return
    
    tasks = load_tasks()
    tasks.append({"name": name, "status": status})
    save_tasks(tasks)
    print(f"Task added: {name} (Status: {status})")

def remove_task(index):
    """Remove a task by its index."""
    tasks = load_tasks()
    try:
        task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task deleted: {task['name']} (Status: {task['status']})")
    except IndexError:
        print(f"Error: No task at index {index}")

def update_status(index, new_status):
    """Update the status of a task by its index."""
    if new_status not in ["Not Started", "Progressing", "Done"]:
        print("Error: Invalid status. Must be 'Not Started', 'Progressing', or 'Done'.")
        return

    tasks = load_tasks()
    try:
        tasks[index]["status"] = new_status
        save_tasks(tasks)
        print(f"Task updated: {tasks[index]['name']} (New Status: {new_status})")
    except IndexError:
        print(f"Error: No task at index {index}")

def display_task(factor="Done"):
    """Display tasks based on their status."""
    if factor not in ["Not Started", "Progressing", "Done"]:
        print("Error: Invalid status. Must be 'Not Started', 'Progressing', or 'Done'.")
        return
    
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks):
            if task['status'] == factor:
                print(f"{i}. {task['name']} (Status: {task['status']})")

def display():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task['name']} (Status: {task['status']})")

def main():
    parser = argparse.ArgumentParser(description="Simple Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("name", type=str, help="Name of the task")
    add_parser.add_argument("--status", type=str, default="Not Started", choices=["Not Started", "Progressing", "Done"], help="Status of the task")

    # Remove task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Index of the task to delete")

    # Update task status command
    update_parser = subparsers.add_parser("update", help="Update a task's status")
    update_parser.add_argument("index", type=int, help="Index of the task to update")
    update_parser.add_argument("status", type=str, choices=["Not Started", "Progressing", "Done"], help="New status of the task")

    # Display all tasks command
    display_parser = subparsers.add_parser("display", help="Display all tasks")

    # Display tasks based on status command
    display_priority_parser = subparsers.add_parser("displayPriority", help="Display tasks based on their status")
    display_priority_parser.add_argument("status", type=str, choices=["Not Started", "Progressing", "Done"], help="Status to filter tasks by")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.name, args.status)
    elif args.command == "delete":
        remove_task(args.index)
    elif args.command == "update":
        update_status(args.index, args.status)
    elif args.command == "display":
        display()
    elif args.command == "displayPriority":
        display_task(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
