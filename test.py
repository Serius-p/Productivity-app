import unittest
from unittest.mock import patch
from goals import Goals
from datetime import date
from menu import Menu
import tempfile
from pathlib import Path
import json

class TestGoals(unittest.TestCase):
    def setUp(self):
        self.goals = Goals()

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
        menu = Menu()
        menu.goals.tasks = [
            {"name": "A", "due_date": date(2026, 1, 2), "status": False}
        ]
        menu.goals.habits = [
            {"name": "Walk", "start_date": date(2026, 1, 3), "frequency": 3}
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            menu.data_file = Path(temp_dir) / "tasks.json"
            menu.data_file2 = Path(temp_dir) / "habits.json"

            menu.save_data()

            with menu.data_file.open(encoding="utf-8") as f:
                saved_tasks = json.load(f)
            with menu.data_file2.open(encoding="utf-8") as f:
                saved_habits = json.load(f)

        self.assertEqual(saved_tasks[0]["due_date"], "2026-01-02")
        self.assertEqual(saved_habits[0]["start_date"], "2026-01-03")
        self.assertEqual(saved_habits[0]["frequency"], 3)

if __name__ == '__main__':
    unittest.main()


#assertEqual    assertNotEqual     assertTrue             assertFalse
#assertIs       assertIsNot        assertIsNone           assertIsNotNone
#assertIn       assertNotIn        assertIsInInstance     assertNotIsInInstance