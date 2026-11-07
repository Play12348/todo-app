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


class TaskManager:
    """Управляет списком дел."""
    def __init__(self):
        self.tasks: list[Task] = []

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

    # Метод для задания со звёздочкой 3.5
    def find_by_title(self, fragment: str) -> list[Task]:
        fragment = fragment.lower()
        return [task for task in self.tasks if fragment in task.title.lower()]