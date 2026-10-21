from goals import Goals

class Menu:
    def __init__(self):
        self.menu_list = ["1.New Goal", "2.View Goals", "3.Exit"]

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
                Goals.add_logic(self)


            if menu_choice == 2:
                pass

            if menu_choice == 3:
                print("Saving data..")
                print("Done!")
                break

start = Menu()
start.menu_options()