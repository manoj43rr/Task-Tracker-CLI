# Task Tracker CLI

Welcome to the Task Tracker CLI! This command-line interface (CLI) application helps you efficiently manage your to-do list and track your tasks. Unlike graphical user interfaces that rely on buttons and visual elements, this CLI app interacts with users solely through commands, offering a powerful way to handle tasks directly from your terminal.

## Features

This application provides the following functionalities:

- **Add Tasks**: Easily add new tasks to your to-do list.
- **Update Tasks**: Modify existing tasks, including changing their status.
- **Delete Tasks**: Remove tasks from your list when they are no longer needed.
- **Mark Tasks**: Update the status of a task to "In Progress" or "Done".
- **List All Tasks**: View all tasks in your list, regardless of their status.
- **Filter by Status**:
  - List all tasks that are marked as "Done".
  - List all tasks that are marked as "Not Started".
  - List all tasks that are "In Progress".

## Project Challenge

This project is inspired by the [Task Tracker Challenge](https://roadmap.sh/projects/task-tracker) on Roadmap.sh. It is designed to provide a practical tool for managing tasks and improving productivity.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Task-Tracker-CLI.git
   cd Task-Tracker-CLI
2. **Install Dependencies:**

  Make sure you have Python installed. Install any required dependencies using:
  
  pip install -r requirements.txt

3. **Run the Application:**

  Use the CLI commands to manage your tasks:

  Add a new task:
  python app.py add "Task Name" --status "Not Started"
  
  Update a task:
  python app.py update <index> --status "In Progress"
  
  Delete a task:
  python app.py delete <index>
  
  Display all tasks:
  python app.py display
  
  Display tasks by status:
  python app.py displayPriority "Done"
  
  **Contributing**
  Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting improvements. Your feedback and contributions are highly appreciated!

***Happy Coding!***

link to project challenge: https://roadmap.sh/projects/task-tracker
