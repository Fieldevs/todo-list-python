import json
import os

filename = "tasks.json"

# Load tasks if file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

while True:
    print("\n=== To-do List ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Show Summary")
    print("6. Quit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        with open(filename, "w") as file:
            json.dump(tasks, file)
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
            try:
                task_number = int(input("Enter the task number to mark as done: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["done"] = True
                    with open(filename, "w") as file:
                        json.dump(tasks, file)
                    print("Task marked as done!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        if not tasks:
            print("No tasks to remove!")
        else:
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    with open(filename, "w") as file:
                        json.dump(tasks, file)
                    print(f"Task '{removed_task['task']}' removed successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":
        total = len(tasks)
        done = sum(task["done"] for task in tasks)
        pending = total - done
        print(f"\nTotal tasks: {total}")
        print(f"Completed: {done}")
        print(f"Pending: {pending}")

    elif choice == "6":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 6.")
