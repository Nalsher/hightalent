import os
from xml.dom import NotFoundErr
from src.repositories.TaskRepository import MockTaskRepository
from src.services.TaskService import TaskService


def console_interface():
    file_path = os.path.join("../storage/tasks.json")
    repository = MockTaskRepository(file_path)
    service = TaskService(repository)

    while True:
        print("\n=== Task Management ===")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List All Tasks")
        print("4. List All Tasks By Category")
        print("5. Find Task")
        print("6. Change Task")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                task_id = int(input("Enter Task ID: "))
                title = input("Enter Task Title: ")
                description = input("Enter Task Description: ")
                date = input("Enter Task Due Date: ")
                category = input("Enter Task Category: ")
                priority = input("Enter Task Priority: ")
                service.create_task(task_id, title, description, category, date, priority)
                print("Task added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                if service.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "3":
            tasks = service.find_all_tasks()
            if tasks:
                print("\nCurrent Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")
        elif choice == "4":
            category = input("Enter Task Category: ")
            tasks = service.find_all_tasks_by_category(category)
            if tasks:
                print("\nCurrent Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")
        elif choice == "5":
            try:
                id = input("Enter Task ID: ")
                category = input("Enter Task Category: ")
                status = input("Enter Task Status: ")
                keyword = input("Enter Task keyword: ")
                print(service.find_task(id, keyword, status, category))
            except NotFoundErr:
                print("Task not found")
        elif choice == "6":
            try:
                id = int(input("Enter Task ID: "))
                task_title = input("Enter New Task Title: ")
                task_description = input("Enter New Task Description: ")
                task_status = input("Enter New Task Status: ")
                if (service.update_task(id, task_title, task_description, task_status)):
                    print("Task changed successfuly")
                else:
                    print("Task not found")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "7":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")


console_interface()
