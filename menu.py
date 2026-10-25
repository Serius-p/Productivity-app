from goals import Goals

class Menu:
    def __init__(self):
        self.menu_list = ["1.New Goal", "2.View Goals", "3.Exit"]
        self.goals = Goals()

    def menu_options(self):

        while True:
            print("\n==Productivity Manager==\n")
            for options in self.menu_list:
                print(options)
            try:
                menu_choice = int(input("\n>>>>>: "))
            except Exception:
                print("Invalid Choice!")
                continue

            if menu_choice == 1:
                print("\nChoose Goal Type:\n1.Task\n2.Habit")
                type_choice = int(input("\n>>>>>: "))
                if type_choice == 1:
                    self.goals.add_logic()
                elif type_choice == 2:
                    print("Habit goals are not implemented yet.")

            if menu_choice == 2:
                if not self.goals.tasks:
                    print("No goals added yet.")
                else:
                    for number, task in enumerate(self.goals.tasks, start=1):
                        print(f"{number}. {task['name']}")

                    decision_2 = False
                    while not decision_2:
                        print(f"{"-"*25}\n1.Edit\n2.View details\n3.Delete\n4.Mark task as complete\n5.Back\n{"-"*25}")
                        try:
                            dec2_choice = int(input("\n>>>>>: "))
                        except Exception:
                            print("Invalid Choice!")
                            continue
                #Choice is edit
                        if dec2_choice == 1:
                            try:
                                edit_choice = int(input("\nChoose task\n>>>>>: "))
                            except ValueError:
                                print("Invalid task number!")
                                continue

                            task_index = edit_choice - 1
                            if 0 <= task_index < len(self.goals.tasks):
                                task = self.goals.tasks[task_index]
                                task["name"] = input("Name: ")
                                task["description"] = input("Description: ")
                                task["date"] = input("Due date: ")
                                print("\nThe task has been updated!")
                            decision_2 = True
                #Choice is view
                        elif dec2_choice == 2:
                            try:
                                view_choice = int(input("\nChoose task\n>>>>>: "))
                            except ValueError:
                                print("Invalid task number!")
                                continue

                            task_index = view_choice - 1
                            if 0 <= task_index < len(self.goals.tasks):
                                #Checks that the choice isn´t negative, also that it´s less than the number of tasks.
                                task = self.goals.tasks[task_index]
                                print(f"\nName: {task['name']}")
                                print(f"Description: {task['description']}")
                                print(f"Due date: {task['date']}")
                                print(f"Completed: {task['status']}")
                            else:
                                print("Invalid task number!")
                                continue
                            decision_2 = True
                #Choice is delete
                        elif dec2_choice == 3:
                            try:
                                del_choice = int(input("\nChoose task\n>>>>>: "))
                            except Exception:
                                print("Invalid task number!")
                                continue

                            task_index = del_choice - 1
                            if 0 <= task_index < len(self.goals.tasks):
                                self.goals.tasks.pop(task_index)
                                print("The task has been deleted!")
                            else:
                                print("Invalid task number!")
                                continue
                            decision_2 = True
                #Choice is Mark task as complete
                        elif dec2_choice == 4:
                            try:
                                mark_choice = int(input("\nChoose task\n>>>>>: "))
                            except Exception:
                                print("Invalid task number!")
                                continue

                            task_index = mark_choice - 1
                            if 0 <= task_index < len(self.goals.tasks):
                                task = self.goals.tasks[task_index]
                                task["status"] = True
                                print("\nTask has been marked as complete!")
                                decision_2 = True
                #Choise is to go back
                        elif dec2_choice == 5:
                            decision_2 = True

            if menu_choice == 3:
                print("Saving data..")
                print("Done!")
                break

start = Menu()
start.menu_options()