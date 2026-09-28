# Command-Line Task Manager Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A fast, lightweight command-line task manager built in Python. Designed for developers and terminal enthusiasts who want to manage local tasks without leaving the command line. Provides full CRUD operations, task filtering, and JSON local persistence.

---

## Key Features

- **Full CRUD Support**: Create, read, update status, and delete tasks directly from your terminal.
- **Local Persistence**: Tasks are saved automatically in a human-readable `tasks.json` storage file.
- **Priority & Status Filtering**: Filter tasks seamlessly by completion state (`pending` or `completed`) and priority level (`A`, `B`, `C`).
- **Formatted Terminal Output**: Uses ANSI color coding and formatted tables for clear visibility.

---
## Features Showcase

| Feature | Description | CLI Command |
| :--- | :--- | :--- |
| **Create Task** | Add new tasks with title and priority levels (`A`, `B`, `C`). | `python todo.py add "<title>" -p <prio>` |
| **List Tasks** | View all active and completed tasks in a styled format. | `python todo.py list` |
| **Filter by Status** | View tasks isolated by `pending` or `completed` state. | `python todo.py list -s pending` |
| **Filter by Priority** | View tasks isolated by priority level (`A`, `B`, or `C`). | `python todo.py list -p A` |
| **Complete Task** | Mark a task as done by its unique ID. | `python todo.py complete <id>` |
| **Delete Task** | Remove a task permanently from local storage. | `python todo.py delete <id>` |
| **JSON Storage** | Auto-saves all changes locally to `tasks.json`. | *Automatic* |

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Gnyaneswar-Reddy/Task-Manager.git](https://github.com/Gnyaneswar-Reddy/Task-Manager.git)
   cd Task-Manager
