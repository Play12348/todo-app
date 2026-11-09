import unittest
from logic import Task, TaskManager

class TestTask(unittest.TestCase):
    class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Этот метод выполняется ПЕРЕД КАЖДЫМ тестом в этом классе
        self.manager = TaskManager()
        self.manager.add_task("Хлеб", "2025-11-01")
        self.manager.add_task("Цветы", "2025-11-03")

    def test_add_and_count(self):
        self.assertEqual(self.manager.count(), 2)

    def test_get_all_returns_copy(self):
        tasks = self.manager.get_all()
        tasks.pop()  # пробуем испортить копию
        # Проверяем, что оригинальный список не пострадал
        self.assertEqual(self.manager.count(), 2)

    def test_mark_done_and_get_pending(self):
        self.manager.mark_done("Хлеб")
        pending = self.manager.get_pending()
        self.assertEqual([t.title for t in pending], ["Цветы"])

    def test_remove_existing(self):
        self.manager.remove_task("Хлеб")
        self.assertEqual(self.manager.count(), 1)

    def test_remove_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.remove_task("Нет такого")

    def test_mark_done_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.mark_done("Нет такого")
    def test_default_not_done(self):
        task = Task("Дело", "2025-11-01")
        self.assertFalse(task.done)

    def test_mark_done(self):
        task = Task("Дело", "2025-11-01")
        task.mark_done()
        self.assertTrue(task.done)

    def test_title_is_stripped(self):
        task = Task("  Хлеб  ", "2025-11-01")
        self.assertEqual(task.title, "Хлеб")

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("", "2025-11-01")

    def test_spaces_only_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2025-11-01")

if __name__ == "__main__":
    unittest.main()