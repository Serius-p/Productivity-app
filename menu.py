from goals import Goals
from datetime import date
import json
from pathlib import Path

class Menu:
    def __init__(self):
        self.menu_list = ["1.New Goal", "2.View Goals", "3.Exit"]
        self.goals = Goals()
        self.today = date.today()
        self.data_file = Path(__file__).with_name("task_data.json")
        self.data_file2 = Path(__file__).with_name("habit_data.json")
    #Loading saved data
    def load_data(self):
        try:
            with self.data_file.open("r") as f:
                self.goals.tasks = json.load(f)
            with self.data_file2.open("r") as f:
                self.goals.habits = json.load(f)
            for task in self.goals.tasks:
                task["due_date"] = date.fromisoformat(task["due_date"])
            for habit in self.goals.habits:
                habit["start_date"] = date.fromisoformat(habit["start_date"])
        except FileNotFoundError:
            print("No saved data found!")

    def save_data(self):
        print("Saving data..")
        with self.data_file.open("w") as f:
            json.dump(self.goals.tasks, f, default=date.isoformat)
        with self.data_file2.open("w") as f:
            json.dump(self.goals.habits, f, default=date.isoformat)
        print("Done!")

    def menu_options(self):

        while True:
            print("\n==Productivity Manager==")
            print(f"Date:{self.today}\n")
            for options in self.menu_list:
                print(options)
            try:
                menu_choice = int(input("\n>>>>>: "))
                if not 1 <= menu_choice <= 3:
                    print("Invalid choice!")
                    continue
            except ValueError:
                print("Invalid Choice!")
                continue

            if menu_choice == 1:
                print("\nChoose Goal Type:\n1.Task\n2.Habit")
                try:
                    type_choice = int(input("\n>>>>>: "))
                    if type_choice == 1:
                        self.goals.add_task()
                        continue
                    elif type_choice == 2:
                        self.goals.add_habit()
                        continue
                except ValueError:
                    print("Invalid input!")
                    continue

            if menu_choice == 2:
                self.goals.goal_exist()

                if not self.goals.goal_exist():
                    print("No goals added yet!")
                elif self.goals.goal_exist():
                    print("--TASKS--")
                    for number, task in enumerate(self.goals.tasks, start=1):
                        print(f"{number}. {task['name']}")
                    print("\n--HABITS--")
                    for number, habit in enumerate(self.goals.habits, start=1):
                        print(f"{number}. {habit["name"]}")

                    decision_2 = False
                    while not decision_2:
                        print(f"{"-"*30}\n1.Edit\n2.View details\n3.Delete\n4.Mark task as complete\n5.Back\n{"-"*30}")
                        try:
                            dec2_choice = int(input(">>>>>: "))
                        except ValueError:
                            print("Invalid Choice!")
                            continue
                #Choice is edit
                        if dec2_choice == 1:
                            edit_choice = self.goals.task_or_habit()
                            if edit_choice == 1:
                                self.goals.edit_task()
                            elif edit_choice == 2:
                                self.goals.edit_habit()
                            decision_2 = True
                #Choice is view
                        elif dec2_choice == 2:
                            edit_choice = self.goals.task_or_habit()                   
                            if edit_choice == 1:
                                self.goals.view_task()
                            elif edit_choice == 2:
                                self.goals.view_habit()
                            decision_2 = True
                #Choice is delete
                        elif dec2_choice == 3:
                            edit_choice = self.goals.task_or_habit()
                            if edit_choice == 1:
                                self.goals.delete_task()
                            elif edit_choice == 2:
                                self.goals.delete_habit()
                            decision_2 = True
                #Choice is Mark task as complete
                        elif dec2_choice == 4:
                            edit_choice = self.goals.task_or_habit()                            
                            if edit_choice == 1:
                                self.goals.complete_task()
                            elif edit_choice == 2:
                                print("Can`t mark habit as complete!")
                            decision_2 = True
                #Choise is to go back
                        elif dec2_choice == 5:
                            decision_2 = True

            if menu_choice == 3:
                self.save_data()
                break

if __name__ == "__main__":
    start = Menu()
    start.menu_options()

#print(f"\n{"-"*30}")