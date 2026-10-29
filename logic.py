class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        self.title = title
        self.deadline = deadline
        self.done = done