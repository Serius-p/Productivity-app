from datetime import date

class Goals:
    def __init__(self):
        self.tasks = []
        self.habits = []

    def add_logic(self):
        name = input("Name: ")
        description = input("Description: ")
        due_date = date.fromisoformat(input("Due date (YYYY-MM-DD): "))
        self.tasks.append({
            "name": name,
            "description": description,
            "date": due_date,
        })
        print("All good")