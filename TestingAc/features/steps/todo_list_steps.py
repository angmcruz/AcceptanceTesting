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


def main():
    """Main function to run the To-Do List Manager"""
    todo_list = TodoList()
    
    print("=" * 50)
    print("Welcome to To-Do List Manager!")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark task as completed")
        print("4. Clear all tasks")
        print("5. Remove a specific task")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            priority = input("Enter priority (Low/Medium/High): ").strip() or "Medium"
            todo_list.add_task(title, description, priority)
            print(f"✓ Task '{title}' added successfully!")
        
        elif choice == "2":
            tasks = todo_list.list_tasks()
            if tasks:
                print("\nYour Tasks:")
                print("-" * 50)
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                    if task.description:
                        print(f"   Description: {task.description}")
            else:
                print("\nYour to-do list is empty!")
        
        elif choice == "3":
            title = input("Enter the task title to mark as completed: ").strip()
            if todo_list.mark_task_completed(title):
                print(f"✓ Task '{title}' marked as completed!")
            else:
                print(f"✗ Task '{title}' not found!")
        
        elif choice == "4":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                todo_list.clear_all()
                print("✓ All tasks cleared!")
            else:
                print("Operation cancelled.")
        
        elif choice == "5":
            title = input("Enter the task title to remove: ").strip()
            if todo_list.remove_task(title):
                print(f"✓ Task '{title}' removed successfully!")
            else:
                print(f"✗ Task '{title}' not found!")
        
        elif choice == "6":
            print("\nThank you for using To-Do List Manager!")
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()