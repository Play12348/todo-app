import os
import tempfile
import unittest
from logic import Task
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        # Создаем временную папку для каждого теста
        self.tmpdir = tempfile.TemporaryDirectory()
        # Формируем путь к временному файлу внутри нее
        self.path = os.path.join(self.tmpdir.name, "tasks.json")
        self.storage = Storage(self.path)

    def tearDown(self):
        # Удаляем временную папку со всеми файлами после теста
        self.tmpdir.cleanup()

    def test_missing_file_returns_empty(self):
        # Если файла нет, load() должен вернуть пустой список
        self.assertEqual(self.storage.load(), [])

    def test_save_and_load_roundtrip(self):
        # Тест на сохранение и загрузку
        tasks = [Task("Хлеб", "2025-11-01", True), Task("Цветы", "2025-11-03")]
        self.storage.save(tasks)
        
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].title, "Хлеб")
        self.assertTrue(loaded[0].done)
        self.assertFalse(loaded[1].done)

    def test_corrupted_file_raises(self):
        # Пишем в файл откровенную чушь
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("это не json")
        
        # Ожидаем ошибку ValueError (JSONDecodeError - его наследник)
        with self.assertRaises(ValueError):
            self.storage.load()

    def test_not_a_list_raises(self):
        # Пишем в файл валидный JSON, но это словарь, а не список
        with open(self.path, "w", encoding="utf-8") as f:
            f.write('{"title": "Вместо списка - словарь"}')
        
        # Ожидаем ошибку, так как ожидался список
        with self.assertRaises(ValueError):
            self.storage.load()

if __name__ == "__main__":
    unittest.main()