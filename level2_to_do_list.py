tasks = []

while True:
    print("\n=== To-do List ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                status = "[Done]" if task["done"] else "[Pending]"
                print(f"{i}. {task['task']} {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done!")
        else:
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        if not tasks:
            print("No tasks to remove!")
        else:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' removed successfully!")
            else:
                print("Invalid task number!")

    elif choice == "5":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")
