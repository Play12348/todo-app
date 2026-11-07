from logic import TaskManager


class ConsoleUI:
    def __init__(self, manager: TaskManager):
        self.manager = manager

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите пункт: ").strip()
            if choice == "1":
                self.add_flow()
            elif choice == "2":
                self.show_all()
            elif choice == "3":
                self.mark_done_flow()
            elif choice == "4":
                self.remove_flow()
            elif choice == "5":
                self.show_pending()
            elif choice == "6":
                self.search_flow()
            elif choice == "0":
                break
            else:
                print("Нет такого пункта меню")

    def print_menu(self):
        print("\n=== Список дел ===")
        print("1. Добавить дело")
        print("2. Показать все дела")
        print("3. Отметить выполненным")
        print("4. Удалить дело")
        print("5. Показать только невыполненные")
        print("6. Поиск по названию")
        print("0. Выход")

    def add_flow(self):
        title = input("Название дела: ").strip()
        deadline = input("Срок (ГГГГ-ММ-ДД): ").strip()
        try:
            self.manager.add_task(title, deadline)
            print("Дело добавлено")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def show_all(self):
        tasks = self.manager.get_all()
        if not tasks:
            print("Список пуст")
        for task in tasks:
            print(task)

    def mark_done_flow(self):
        title = input("Название дела для отметки: ").strip()
        try:
            self.manager.mark_done(title)
            print("Дело отмечено как выполненное")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def remove_flow(self):
        title = input("Название дела для удаления: ").strip()
        try:
            self.manager.remove_task(title)
            print("Дело удалено")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def show_pending(self):
        tasks = self.manager.get_pending()
        if not tasks:
            print("Нет невыполненных дел")
        for task in tasks:
            print(task)

    def search_flow(self):
        fragment = input("Введите часть названия для поиска: ").strip()
        tasks = self.manager.find_by_title(fragment)
        if not tasks:
            print("Ничего не найдено")
        for task in tasks:
            print(task)