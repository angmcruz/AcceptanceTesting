class Task:
    """Represents a single task in the to-do list"""
    
    def __init__(self, title, description="", priority="Medium", status="Pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    
    def mark_completed(self):
        """Mark this task as completed"""
        self.status = "Completed"
    
    def __str__(self):
        return f"[{self.status}] {self.title} (Priority: {self.priority})"
    
    def __repr__(self):
        return self.__str__()


class TodoList:
    """Manages a collection of tasks"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description="", priority="Medium"):
        """Add a new task to the list"""
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task
    
    def list_tasks(self):
        """Return all tasks in the list"""
        return self.tasks
    
    def mark_task_completed(self, title):
        """Mark a specific task as completed by title"""
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False
    
    def clear_all(self):
        """Remove all tasks from the list"""
        self.tasks.clear()
    
    def is_empty(self):
        """Check if the to-do list is empty"""
        return len(self.tasks) == 0
    
    def get_task_by_title(self, title):
        """Get a specific task by its title"""
        for task in self.tasks:
            if task.title == title:
                return task
        return None
    
    def remove_task(self, title):
        """Remove a specific task from the list"""
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False
    
    def get_pending_tasks(self):
        """Return only pending tasks"""
        return [task for task in self.tasks if task.status == "Pending"]
    
    def get_completed_tasks(self):
        """Return only completed tasks"""
        return [task for task in self.tasks if task.status == "Completed"]


