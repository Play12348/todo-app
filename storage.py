import json
from logic import Task

class Storage:
    """Отвечает за чтение и запись списка дел в файл."""
    
    def __init__(self, path: str = "tasks.json"):
        self.path = path
        
    def save(self, tasks: list[Task]) -> None:
        data = [task.to_dict() for task in tasks]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    def load(self) -> list[Task]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
            
        if not isinstance(data, list):
            raise ValueError("Хранилище повреждено: ожидается список дел")
            
        return [Task.from_dict(item) for item in data]