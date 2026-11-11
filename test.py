import unittest
from unittest.mock import patch
from goals import Goals
from datetime import date
from menu import Menu

class TestGoals(unittest.TestCase):
    def setUp(self):
        self.goals = Goals()
        self.menu = Menu()

    def test_goal_exist_none(self):
        self.assertFalse(self.goals.goal_exist())

    def test_goal_exist_h(self):
        self.goals.habits.append({"name":"LoL"})

        self.assertTrue(self.goals.goal_exist())

    def test_goal_exist_t(self):
        self.goals.tasks.append({"name":"LoL"})

        self.assertTrue(self.goals.goal_exist())

    def test_complete_task(self):
        self.goals.tasks.append({"name":"LoL", "status": False,})

        with patch("builtins.input", return_value ="1"):
            self.goals.complete_task()
        
        self.assertTrue(self.goals.tasks[0]["status"])

    def test_delete_task(self):
        self.goals.tasks.append({"name":"LoL"})

        with patch("builtins.input", return_value = "1"):
            self.goals.delete_task()

        self.assertFalse(self.goals.tasks)

    def test_add_habit_rejects_frequency_outside_range(self):
        today = date.today().isoformat()

        with patch("builtins.input", side_effect=[
            "A", "B", today, "8",  # First attempt: invalid frequency
            "A", "B", today, "3",  # Retry: valid frequency
        ]):
            self.goals.add_habit()

        self.assertEqual(len(self.goals.habits), 1)
        self.assertEqual(self.goals.habits[0]["frequency"], 3)

    def test_edit_task(self):
        today = date.today().isoformat()
        self.goals.tasks.append({"name":"A", "description":"B", "due_date":today})

        with patch("builtins.input", side_effect=[
            1, "Task", "Description B", today,
        ]):
            self.goals.edit_task()

        self.assertEqual(self.goals.tasks[0]["name"], "Task")
        self.assertEqual(self.goals.tasks[0]["description"], "Description B")

    def test_data_saves(self):
        self.goals.tasks.append({"name":"A"})

        with patch("builtins.input", return_value=3):
            self.menu.menu_options()

        self.assertEqual(len(self.goals.tasks), 1)
        self.assertEqual(self.goals.tasks[0]["name"], "A")

if __name__ == '__main__':
    unittest.main()


#assertEqual    assertNotEqual     assertTrue             assertFalse
#assertIs       assertIsNot        assertIsNone           assertIsNotNone
#assertIn       assertNotIn        assertIsInInstance     assertNotIsInInstance