import json  # Import the JSON module to save and load tasks from a file
import os    # Import the OS module to check if the file exists

filename = "tasks.json"  # Name of the file where tasks will be persisted

# Load tasks from file if it exists; otherwise start with an empty list
if os.path.exists(filename):                    # Check if the tasks file already exists
    with open(filename, "r") as file:           # Open the file in read mode
        tasks = json.load(file)                 # Parse JSON content into the 'tasks' list
else:
    tasks = []                                  # Initialize an empty list if no file is found

# Main program loop that keeps the menu running
while True:
    print("\n=== To-do List ===")               # Header for the menu
    print("1. Add Task")                        # Menu option to add a new task
    print("2. Show Tasks")                      # Menu option to display all tasks
    print("3. Mark Task as Done")               # Menu option to mark a task as completed
    print("4. Remove Task")                     # Menu option to delete a task
    print("5. Show Summary")                    # Menu option to show basic statistics
    print("6. Quit")                            # Menu option to exit the program

    choice = input("Choose an option (1-6): ")  # Read the user's menu choice as a string

    if choice == "1":                           # If the user chose to add a task
        task = input("Enter a new task: ")      # Ask the user to type the task description
        tasks.append({"task": task, "done": False})  # Add a new task with status 'False' (pending)
        with open(filename, "w") as file:       # Open the file in write mode to persist changes
            json.dump(tasks, file)              # Save the updated tasks list to JSON
        print("Task added successfully!")       # Confirmation message

    elif choice == "2":                         # If the user chose to show tasks
        if not tasks:                           # If the list is empty, inform the user
            print("No tasks found!")
        else:
            print("\nYour tasks:")              # Title for the tasks list
            for i, task in enumerate(tasks, 1): # Loop through tasks with a 1-based index
                status = "[Done]" if task["done"] else "[Pending]"  # Choose label based on status
                print(f"{i}. {task['task']} {status}")              # Print index, text, and status

    elif choice == "3":                         # If the user chose to mark a task as done
        if not tasks:                           # If there are no tasks, nothing to mark
            print("No tasks to mark as done!")
        else:
            try:
                # Try to convert the input to an integer; this may raise ValueError
                task_number = int(input("Enter the task number to mark as done: "))
                if 1 <= task_number <= len(tasks):     # Ensure the number is within list bounds
                    tasks[task_number - 1]["done"] = True  # Update the task status to done
                    with open(filename, "w") as file:      # Persist the change to disk
                        json.dump(tasks, file)              # Save the entire tasks list again
                    print("Task marked as done!")           # Confirmation message
                else:
                    print("Invalid task number!")           # Out-of-range number handling
            except ValueError:
                print("Please enter a valid number!")       # Non-numeric input handling

    elif choice == "4":                         # If the user chose to remove a task
        if not tasks:                           # If there are no tasks, nothing to remove
            print("No tasks to remove!")
        else:
            try:
                # Try to read and convert the input to an integer
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):         # Validate the index range
                    removed_task = tasks.pop(task_number - 1)  # Remove the selected task
                    with open(filename, "w") as file:      # Persist the updated list
                        json.dump(tasks, file)              # Save to the JSON file
                    print(f"Task '{removed_task['task']}' removed successfully!")  # Feedback
                else:
                    print("Invalid task number!")           # Out-of-range number handling
            except ValueError:
                print("Please enter a valid number!")       # Non-numeric input handling

    elif choice == "5":                         # If the user chose to show the summary
        total = len(tasks)                      # Total number of tasks
        done = sum(task["done"] for task in tasks)  # Count tasks marked as done (True evaluates to 1)
        pending = total - done                  # Remaining tasks are pending
        print(f"\nTotal tasks: {total}")        # Show total
        print(f"Completed: {done}")             # Show completed count
        print(f"Pending: {pending}")            # Show pending count

    elif choice == "6":                         # If the user chose to quit
        print("Exiting... Goodbye!")            # Friendly exit message
        break                                   # Break the loop to end the program

    else:
        # Handle any input that is not one of the defined options
        print("Invalid choice! Please choose between 1 and 6.")
