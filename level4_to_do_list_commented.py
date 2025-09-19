import json  # Import JSON to read/write tasks in a file
import os    # Import OS to check if the file exists

filename = "tasks.json"  # File name where tasks will be stored

# Load tasks from the file (if it exists), otherwise return an empty list
def load_tasks():
    if os.path.exists(filename):             # Check if the JSON file already exists
        with open(filename, "r") as file:    # Open the file in read mode
            return json.load(file)           # Load tasks from the JSON file
    return []                                # If no file, return an empty list

# Save the current list of tasks to the JSON file
def save_tasks(tasks):
    with open(filename, "w") as file:        # Open the file in write mode
        json.dump(tasks, file)               # Save the list of tasks into JSON format

# Add a new task to the list
def add_task(tasks):
    task = input("Enter a new task: ")       # Ask the user for a task description
    tasks.append({"task": task, "done": False})  # Add the new task with "done" set to False
    save_tasks(tasks)                        # Save changes to the file
    print("Task added successfully!")        # Confirmation message

# Show all tasks with their current status
def show_tasks(tasks):
    if not tasks:                            # If the list is empty
        print("No tasks found!")             # Display message
    else:
        print("\nYour tasks:")               # Header for tasks
        for i, task in enumerate(tasks, 1):  # Loop through tasks with index starting at 1
            status = "[Done]" if task["done"] else "[Pending]"  # Status depends on 'done' value
            print(f"{i}. {task['task']} {status}")              # Show number, description, status

# Mark a selected task as completed
def mark_task_done(tasks):
    if not tasks:                            # If there are no tasks
        print("No tasks to mark as done!")   # Display message
        return
    try:
        task_number = int(input("Enter the task number to mark as done: "))  # Get task number
        if 1 <= task_number <= len(tasks):   # Check if the number is valid
            tasks[task_number - 1]["done"] = True  # Update the task status to done
            save_tasks(tasks)                # Save changes to the file
            print("Task marked as done!")    # Confirmation message
        else:
            print("Invalid task number!")    # If number is outside valid range
    except ValueError:                       # If input is not a valid number
        print("Please enter a valid number!")

# Remove a task from the list
def remove_task(tasks):
    if not tasks:                            # If there are no tasks
        print("No tasks to remove!")         # Display message
        return
    try:
        task_number = int(input("Enter the task number to remove: "))  # Get task number
        if 1 <= task_number <= len(tasks):   # Check if the number is valid
            removed_task = tasks.pop(task_number - 1)  # Remove the task from the list
            save_tasks(tasks)                # Save changes to the file
            print(f"Task '{removed_task['task']}' removed successfully!")  # Confirmation message
        else:
            print("Invalid task number!")    # If number is outside valid range
    except ValueError:                       # If input is not a valid number
        print("Please enter a valid number!")

# Main function that runs the program loop
def main():
    tasks = load_tasks()                     # Load existing tasks at program start
    while True:
        print("\n=== To-do List ===")        # Menu header
        print("1. Add Task")                 # Option to add
        print("2. Show Tasks")               # Option to show
        print("3. Mark Task as Done")        # Option to mark done
        print("4. Remove Task")              # Option to remove
        print("5. Quit")                     # Option to quit

        choice = input("Choose an option (1-5): ")  # Read user input

        if choice == "1":                    # Call add_task if user chose 1
            add_task(tasks)
        elif choice == "2":                  # Call show_tasks if user chose 2
            show_tasks(tasks)
        elif choice == "3":                  # Call mark_task_done if user chose 3
            mark_task_done(tasks)
        elif choice == "4":                  # Call remove_task if user chose 4
            remove_task(tasks)
        elif choice == "5":                  # Exit program if user chose 5
            print("Exiting... Goodbye!")
            break
        else:                                # Handle invalid menu choices
            print("Invalid choice! Please choose between 1 and 5.")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
