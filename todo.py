import argparse
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(title, priority):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "priority": priority.upper(),
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(Fore.GREEN + f"Task #{new_id} added successfully!")

def list_tasks(priority=None, status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    # Filter by completion status
    if status == "completed":
        tasks = [t for t in tasks if t["completed"]]
    elif status == "pending":
        tasks = [t for t in tasks if not t["completed"]]

    # Filter by priority
    if priority:
        tasks = [t for t in tasks if t["priority"] == priority.upper()]

    if not tasks:
        print("No tasks matching criteria.")
        return

    print("\n--- TASK LIST ---")
    for t in tasks:
        status_str = Fore.GREEN + "[DONE]" if t["completed"] else Fore.YELLOW + "[PENDING]"
        prio_str = Fore.CYAN + f"({t['priority']})"
        print(f"{t['id']}. {status_str} {prio_str} {t['title']}")

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_tasks(tasks)
            print(Fore.GREEN + f"Task #{task_id} marked as completed.")
            return
    print(Fore.RED + f"Task #{task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print(Fore.RED + f"Task #{task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(Fore.RED + f"Task #{task_id} deleted successfully.")

def main():
    parser = argparse.ArgumentParser(description="Command-Line Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", type=str, help="Title of the task")
    add_parser.add_argument("-p", "--priority", type=str, default="C", help="Priority (A/B/C)")

    # List command
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("-p", "--priority", type=str, help="Filter by priority")
    list_parser.add_argument("-s", "--status", choices=["completed", "pending"], help="Filter by status")

    # Complete command
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int, help="Task ID to complete")

    # Delete command
    del_parser = subparsers.add_parser("delete")
    del_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.priority)
    elif args.command == "list":
        list_tasks(args.priority, args.status)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
