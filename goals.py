from datetime import date

class Goals:
    def __init__(self):
        self.tasks = []
        self.habits = []
        self.today = date.today()

    def task_or_habit(self):
        toh_choosen = False
        while not toh_choosen:
            try:
                choice = int(input("\n1.Task\n2.Habit\n>>>>>: "))
                if choice == 1:
                    return 1
                elif choice == 2:
                    return 2
                else:
                    print("Invalid choice!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue

    def goal_exist(self):
        if self.tasks:
            return 2
        elif self.habits:
            return 2
        else:
            return 1

    def add_task(self):
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

    def add_habit(self):
        habit_added = False
        while not habit_added:
            try:
                name = input("Name: ")
                description = input("Description: ")
                start_date = date.fromisoformat(input("Start date (YYYY-MM-DD): "))
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

    def edit_task(self):
        if not self.tasks:
            print("No tasks added!")
            return breakpoint
        else: pass
        task_edited = False
        while not task_edited:
            try:
                task_choice = int(input("\nChoose task\n>>>>>: "))
                task_index = task_choice - 1
                if 0 <= task_index < len(self.tasks):
                    task = self.tasks[task_index]
                    task["name"] = input("Name: ")
                    task["description"] = input("Description: ")
                    task["date"] = date.fromisoformat(input("Due date (YYYY-MM-DD): "))
                    print("\nThe task has been updated!")
                    task_edited = True
                else:
                    print("Invalid choice!")
                    continue
            except Exception:
                print("Invalid input!")
                continue

    def view_task(self):
        if not self.tasks:
            print("No tasks added!")
            return breakpoint
        else: pass
        task_viewed = False
        while not task_viewed:
            try:
                task_choice = int(input("\nChoose task\n>>>>>: "))
                task_index = task_choice - 1
                #Checks that the choice isn´t negative, also that it´s less than the number of tasks.
                if 0 <= task_index < len(self.tasks):
                    task = self.tasks[task_index]
                    print(f"\n{"-"*30}")
                    print(f"Name: {task['name']}")
                    print(f"Description: {task['description']}")
                    print(f"Due date: {task['date']}")
                    print(f"Completed: {task['status']}")
                    print(f"Deadline in: {(task["date"]-self.today).days} days")
                    print(f"{"-"*30}")
                    task_viewed = True
                else:
                    print("Invalid task number!")
                    continue
            except Exception:
                print("Invalid input!")
                continue

    def delete_task(self):
        if not self.tasks:
            print("No tasks added!")
            return breakpoint
        else: pass
        task_deleted = False
        while not task_deleted:
            try:
                task_choice = int(input("\nChoose task\n>>>>>: "))
                task_index = task_choice - 1
                if 0 <= task_index < len(self.tasks):
                    self.tasks.pop(task_index)
                    print("The task has been deleted!")
                    task_deleted = True
                else:
                    print("Invalid task number!")
                    continue
            except Exception:
                print("Invalid input!")
                continue

    def complete_task(self):
        if not self.tasks:
            print("No tasks added!")
            return breakpoint
        else: pass
        task_complete = False
        while not task_complete:
            try:
                task_choice = int(input("\nChoose task\n>>>>>: "))
                task_index = task_choice - 1
                if 0 <= task_index < len(self.tasks):
                    task = self.tasks[task_index]
                    task["status"] = True
                    print("\nTask has been marked as complete!")
                    task_complete = True
                else:
                    print("Invalid task number!")
                    continue
            except Exception:
                print("Invalid input!")
                continue
#--------------------------------------HABIT EDITOR----------------------------------#

    def edit_habit(self):
        if not self.habits:
            print("No habits added!")
            return breakpoint
        else: pass
        habit_edited = False
        while not habit_edited:
            try:
                habit_choice = int(input("\nChoose habit\n>>>>>: "))
                habit_index = habit_choice - 1
                if 0 <= habit_index < len(self.habits):
                    habit = self.habits[habit_index]
                    habit["name"] = input("Name: ")
                    habit["description"] = input("Description: ")
                    habit["start_date"] = date.fromisoformat(input("Start date (YYYY-MM-DD): "))
                    if habit["start_date"] < date.today():
                        print("Invalid date!")
                        continue
                    habit["frequency"] = int(input("Practice Frequency / Week: "))
                    if habit["frequency"] > 7:
                        print("Invalid input!")
                        continue
                    else:
                        print("\nThe habit has been updated!")
                        habit_edited = True
            except Exception:
                print("Invalid input!")
                continue

    def view_habit(self):
        if not self.habits:
            print("No habits added!")
            return breakpoint
        else: pass
        habit_viewed = False
        while not habit_viewed:
            try:
                habit_choice = int(input("\nChoose habit\n>>>>>: "))
                habit_index = habit_choice - 1
                if 0 <= habit_index < len(self.habits):
                    habit = self.habits[habit_index]
                    print(f"\n{"-"*30}")
                    print(f"Name: {habit["name"]}")
                    print(f"Description: {habit["description"]}")
                    print(f"Start date: {habit["start_date"]}")
                    print(f"Practice Frequency / Week: {habit["frequency"]}")
                    print(f"{"-"*30}")
                    habit_viewed = True
                else:
                    print("Invalid choice!")
                    continue
            except Exception:
                print("Invaid input!")
                continue

    def delete_habit(self):
        if not self.habits:
            print("No habits added!")
            return breakpoint
        else: pass
        habit_deleted = False
        while not habit_deleted:
            try:
                habit_choice = int(input("\nChoose habit\n>>>>>: "))
                habit_index = habit_choice - 1
                if 0 <= habit_index < len(self.habits):
                    self.habits.pop(habit_index)
                    print("The habit has been deleted!")
                    habit_deleted = True
                else:
                    print("Invalid choice!")
                    continue
            except Exception:
                print("Invalid input!")
                continue