import unittest
from goals import Goals
goals = Goals()

class TestGoals(unittest.TestCase):

    def test_goal_exist(self):
        self.assertFalse(goals.goal_exist())

    def test_complete_task(self):
        self.assertTrue(goals.complete_task())

    def test_delete_task(self):
        pass


if __name__ == '__main__':
    unittest.main()


#assertEqual    assertNotEqual     assertTrue             assertFalse
#assertIs       assertIsNot        assertIsNone           assertIsNotNone
#assertIn       assertNotIn        assertIsInInstance     assertNotIsInInstance