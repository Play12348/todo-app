import unittest
from logic import Task, TaskManager


class TestTask(unittest.TestCase):
    def test_mark_done(self):
        task = Task("Дело", "2025-11-01")
        self.assertFalse(task.done)
        task.mark_done()
        self.assertTrue(task.done)

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2025-11-01")


class TestTaskManager(unittest.TestCase):
    def test_add_and_count(self):
        m = TaskManager()
        m.add_task("Дело 1", "2025-11-01")
        m.add_task("Дело 2", "2025-11-02")
        self.assertEqual(m.count(), 2)

    def test_remove_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(ValueError):
            m.remove_task("Нет такого")


if __name__ == "__main__":
    unittest.main()