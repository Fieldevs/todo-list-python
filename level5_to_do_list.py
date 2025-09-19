import json
import os

filename = "tasks.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "[Done]" if task["done"] else "[Pending]"
            print(f"{i}. {task['task']} {status}")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done!")
        return
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove!")
        return
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def show_summary(tasks):
    total = len(tasks)
    done = sum(task["done"] for task in tasks)
    pending = total - done
    print(f"\nTotal tasks: {total}")
    print(f"Completed: {done}")
    print(f"Pending: {pending}")

def main():
    tasks = load_tasks()
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
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            show_summary(tasks)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
