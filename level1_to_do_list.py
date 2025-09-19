tasks = []  

while True: 
    print("\n=== To-do List ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        task = input("Enter a new task: ")  
        tasks.append(task)  
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):  
            print(f"{i}. {task}")

    elif choice == "3":
        print("Exiting... Goodbye!")
        break  

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
