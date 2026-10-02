tasks = []

while True:
    print("To do List App")
    print("1. View a task")
    print("2. Add a task")
    print("3. Remove a Task")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4) "))

    if choice == 1:
        for i in tasks:
            print(i)

    elif choice == 2:
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task "+task + "added successfully")


    else:
        print("Invalid Input")



