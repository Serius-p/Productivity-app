from datetime import date

class Goals:
    def __init__(self):
        self.tasks = []
        self.habits = []

    def add_logic(self):
        task_added = False
        while not task_added:
            try:
                name = input("Name: ")
                description = input("Description: ")
                due_date = date.fromisoformat(input("Due date (YYYY-MM-DD): "))
            except Exception:
                print("Invalid input!\n ")
                continue
            task_added = True
        self.tasks.append({
            "name": name,
            "description": description,
            "date": due_date,
            "status": False,
        })
        
        print("\nThe task has been added!")