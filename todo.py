tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Add task  2. Show tasks  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break