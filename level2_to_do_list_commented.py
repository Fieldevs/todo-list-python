tasks = []  # List to store all tasks

while True:
    # Display the menu options
    print("\n=== To-do List ===")
    print("1. Add Task")          # Option to add a new task
    print("2. Show Tasks")        # Option to show all tasks
    print("3. Mark Task as Done") # Option to mark a task as completed
    print("4. Remove Task")       # Option to remove a task
    print("5. Quit")              # Option to exit the program

    choice = input("Choose an option (1-5): ")  # Get user choice

    if choice == "1":
        task = input("Enter a new task: ")  # Ask for the new task
        tasks.append({"task": task, "done": False})  # Store task with status False (pending)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:  # Check if the task list is empty
            print("No tasks found!")
        else:
            print("\nYour tasks:")
            # Iterate through the task list and display each task with status
            for i, task in enumerate(tasks, 1):
                status = "[Done]" if task["done"] else "[Pending]"
                print(f"{i}. {task['task']} {status}")

    elif choice == "3":
        if not tasks:  # Check if there are tasks to mark
            print("No tasks to mark as done!")
        else:
            task_number = int(input("Enter the task number to mark as done: "))  # Get task number
            if 1 <= task_number <= len(tasks):  # Validate task number
                tasks[task_number - 1]["done"] = True  # Mark task as done
                print("Task marked as done!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        if not tasks:  # Check if there are tasks to remove
            print("No tasks to remove!")
        else:
            task_number = int(input("Enter the task number to remove: "))  # Get task number
            if 1 <= task_number <= len(tasks):  # Validate task number
                removed_task = tasks.pop(task_number - 1)  # Remove task from list
                print(f"Task '{removed_task['task']}' removed successfully!")
            else:
                print("Invalid task number!")

    elif choice == "5":
        print("Exiting... Goodbye!")  # Exit message
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")  # Handle invalid menu option
