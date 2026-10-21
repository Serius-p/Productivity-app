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

            if menu_choice == 3:
                print("Saving data..")
                print("Done!")
                break

start = Menu()
start.menu_options()