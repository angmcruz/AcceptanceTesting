class Task:
    def __init__(self, title, description="", priority="Medium", status="Pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def mark_completed(self):
        self.status = "Completed"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority="Medium", status="Pending"):
        task = Task(title, description, priority, status)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def clear_tasks(self):
        self.tasks = []
        return True

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False
