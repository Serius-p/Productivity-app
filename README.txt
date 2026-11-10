The user can add tasks with a due date, mark it as complete and delete by choice.
The user can also add habits with a start date, add a wished practice frequency/week.
Both tasks and habits are stored in containers and can be viewed any time with the help of the MAIN MENU.
The tasks and habits are saved with JSON when the user exits the app from the MAIN MENU.
The tasks and habits are also loaded when opening the app.

Note: If the user simply closes the app, the added tasks/habits won´t be saved!

MENU Explanation:
6-24 - Initiating imported things, as well as loading saved data if exists.

26-40 - Initiating Menu the user will see, and giving choice between fist choices; add/view task, save and exit.

42-54 - Simply giving choice to user what type of goal to add, task or habit.

56-111 - First printing the added tasks & habits if exists, then depending on the users choice, calling
         functions to execute edit/view/delete/mark as complete

113-120 - Saving data and exiting

GOALS Explanation:
3-7 - Initiating containers for tasks and habits, as well as importing time.

Function on line:

9 - Let´s the user choose between task or habit before any further action.

25 - A helping function for the "VIEW TASKS" in MENU, checks if there tasks or habits exists.

33 - Adding a task, first validating the input, if successfull, adding it to tasks container.

56 - Addind habit, same as adding task, but instead of due date - start date + frequency.

84 - Editing task, validating first, then updating the tasks container.

112 - Printing all details about task.

140 - Deleting task.

161 - Marking task as complete.

184 - Editing habit, validating first, then updating the habits container.

220 - Printing details about habit.

246 - Deleting habit.