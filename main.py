from ui import ConsoleUI
from logic import TaskManager
from storage import Storage

def main():
    # Создаем хранилище (файл tasks.json)
    storage = Storage("tasks.json")
    
    # Передаем хранилище менеджеру
    manager = TaskManager(storage)
    
    # Загружаем данные
    try:
        manager.load()
    except ValueError as e:
        print(f"Предупреждение: {e}")
        print("Начинаем с пустого списка дел")
        
    # Запускаем интерфейс
    ui = ConsoleUI(manager)
    ui.run()
    
    # Сохраняем данные после выхода из интерфейса
    manager.save()
    print("Данные сохранены")

if __name__ == "__main__":
    main()