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
                if due_date < date.today():
                    print("Invalid date!\n")
                    continue
                else: pass
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

    def add_logic2(self):
        habit_added = False
        while not habit_added:
            try:
                name = input("Name: ")
                description = input("Description: ")
                start_date = date.fromisoformat(input("Start date: "))
                if start_date < date.today():
                    print("Invalid date!\n")
                    continue
                else: pass
                frequency = int(input("Practice Frequency / Week: "))
                if frequency >= 8:
                    print("Invalid input!\n")
                    continue
                else: pass
            except Exception:
                print("Invalid input!\n")
                continue
            habit_added = True
        self.habits.append({
            "name": name,
            "description": description,
            "start_date": start_date,
            "frequency": frequency,
        })
        print("\nThe habit has been added!")
