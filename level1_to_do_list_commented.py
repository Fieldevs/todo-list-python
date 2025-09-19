# to_do_list_level1_commented.py
# To-Do List - Level 1 (add and list tasks)

tasks = []  # Initialize an empty list to store tasks entered by the user

while True:  # Start an infinite loop to keep showing the menu until the user quits
    print("\n=== To-Do List ===")  # Display the app title
    print("1. Add task")  # Show menu option 1
    print("2. Show tasks")  # Show menu option 2
    print("3. Quit")  # Show menu option 3

    choice = input("Choose an option (1-3): ")  # Read the user's menu choice as text

    if choice == "1":  # If the user chose option 1 (add task)
        task = input("Enter a new task: ")  # Ask for the task description
        tasks.append(task)  # Store the task at the end of the list
        print("Task added successfully!")  # Confirm to the user

    elif choice == "2":  # If the user chose option 2 (list tasks)
        print("\nYour tasks:")  # Section header for the tasks list
        for i, task in enumerate(tasks, 1):  # Iterate over tasks with a 1-based index
            print(f"{i}. {task}")  # Print each task with its number

    elif choice == "3":  # If the user chose option 3 (quit)
        print("Exiting... Goodbye!")  # Friendly exit message
        break  # Break the loop to end the program

    else:  # If the user typed anything other than 1, 2, or 3
        print("Invalid choice! Please choose 1, 2, or 3.")  # Show an error message
