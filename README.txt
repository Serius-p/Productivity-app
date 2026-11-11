# Productivity Manager

A simple command-line productivity application written in Python. It allows users to manage tasks and habits, track deadlines, and store their data locally using JSON files.

## Features

### Tasks
- Create tasks with a name, description, and due date.
- View task details and deadlines.
- Edit and delete tasks.
- Mark tasks as completed.

### Habits
- Create habits with a name, description, and start date.
- Set a desired practice frequency between 1 and 7 days per week.
- View, edit, and delete habits.

### Data Storage
- Tasks and habits are stored locally in separate JSON files.
- Saved data is loaded when the application starts.
- Data is saved when the user exits through the main menu.

**Important:** Closing the application without using the exit option may result in unsaved changes.

## Requirements

- Python 3

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   `python menu.py`

## Project Structure

- `menu.py` — Main menu, application flow, and data persistence.
- `goals.py` — Task and habit management.
- `test.py` — Unit tests.
- `task_data.json` — Stored task data.
- `habit_data.json` — Stored habit data.
