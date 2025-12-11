from todo_list import ToDoList

todo = ToDoList()

def menu():
    while True:
        print("\n---- TO DO LIST ----")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task completed")
        print("4. Clear list")
        print("5. Delete task")
        print("6. Exit")

        option = input("Choose: ")

        if option == "1":
            title = input("Task title: ")
            desc = input("Description: ")
            prio = input("Priority (Low/Medium/High): ")
            todo.add_task(title, desc, prio)
            print("Task added!")

        elif option == "2":
            tasks = todo.list_tasks()
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTasks:")
                for t in tasks:
                    print(f"- {t.title} | {t.status} | Priority: {t.priority}")

        elif option == "3":
            title = input("Task to mark as completed: ")
            if todo.mark_completed(title):
                print("Task completed!")
            else:
                print("Task not found.")

        elif option == "4":
            todo.clear_tasks()
            print("All tasks cleared.")

        elif option == "5":
            title = input("Task to delete: ")
            if todo.delete_task(title):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif option == "6":
            break

menu()
