
tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' has been added to your to-do list.")

    elif choice == '2':
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet! 🎉")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        print("\nWhich task do you want to remove?")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter the task number: "))
            removed = tasks.pop(task_num - 1)
            print(f"❌ '{removed}' has been removed.")
        except (ValueError, IndexError):
            print("⚠️ Invalid number, please try again.")

    elif choice == '4':
        print("Goodbye! 👋")
        break

    else:
        print("⚠️ Please enter a number between 1 and 4.")
