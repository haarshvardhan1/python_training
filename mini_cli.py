# todo application
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:

            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    description = input("Enter task description : ").strip()

    task = {"id": len(tasks) + 1, "description": description, "done": False}
    tasks.append(task)
    print(f"Task added: {description} \n")


def view_task(tasks):
    if not tasks:
        print("No Task yet. Add one!\n")
        return

    print("\n --- Your Tasks ---")
    for task in tasks:
        status = "✅ Done" if task["done"] else "❌ Pending"
        print(f"[{task['id']}] {task['description']} - {status}")


def show_menu():
    print("===========Task Manger=========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("==============================")


def main():
    tasks = load_tasks()
    print("Welcome to your Task Manager! \n")

    show_menu()
    choice = input("Choose an option (1-5) : ").strip()

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_task(tasks)

    save_tasks(tasks)
    print("Goodbye")


if __name__ == "__main__":
    main()
