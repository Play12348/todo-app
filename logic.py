class Task:
    """Дело в списке дел."""
    
    def __init__(self, title: str, deadline: str, done: bool = False):
        if not title or not title.strip():
            raise ValueError("Название дела не может быть пустым")
        self.title = title.strip()
        self.deadline = deadline
        self.done = done

    def mark_done(self) -> None:
        self.done = True

    def __str__(self) -> str:
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title} (срок: {self.deadline})"

    def to_dict(self) -> dict:
        return {
            "title": self.title, 
            "deadline": self.deadline, 
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            data["title"], 
            data["deadline"], 
            data.get("done", False)
        )


class TaskManager:
    """Управляет списком дел."""
    
    def __init__(self, storage=None):
        self.storage = storage
        self.tasks: list[Task] = []
        
    def load(self) -> None:
        if self.storage is not None:
            self.tasks = self.storage.load()
            
    def save(self) -> None:
        if self.storage is not None:
            self.storage.save(self.tasks)

    def add_task(self, title: str, deadline: str) -> Task:
        task = Task(title, deadline)
        self.tasks.append(task)
        return task

    def remove_task(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        raise ValueError(f"Дело «{title}» не найдено")

    def mark_done(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return
        raise ValueError(f"Дело «{title}» не найдено")

    def get_all(self) -> list[Task]:
        return list(self.tasks)

    def get_pending(self) -> list[Task]:
        return [task for task in self.tasks if not task.done]

    def count(self) -> int:
        return len(self.tasks)

    # --- НОВЫЙ МЕТОД ДЛЯ ЛАБЫ 7 ---
    def get_sorted_by_deadline(self) -> list[Task]:
        return sorted(self.tasks, key=lambda t: t.deadline)