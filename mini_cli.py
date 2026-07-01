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


# tasks = []


def add_task(tasks):

    name = input("Enter task name : ").strip()
    description = input("Enter task description : ").strip()

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "description": description,
        "done": False,
    }
    tasks.append(task)
    print(f"✅ Task added with name {name} \n")


def view_task(tasks):
    if not tasks:
        print("No Task yet. Add one!\n")
        return

    print("\n -------------------- Your Tasks ---------------------")
    for task in tasks:
        status = "✅ Done" if task["done"] else "❌ Pending"
        print(
            f"[{task['id']}] Task Name : {task['name']} \n \t Task Description : {task['description']} \n \t Status: {status} \n"
        )
    print("*********************************************** \n\n")


def mark_task_done(tasks):
    if not tasks:
        return

    task_id = int(input("Enter task ID to mark as done : ").strip())

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"🎉 Task {task_id} marked as done!")
            return

    print(f"⚠️ No task found with ID {task_id}. \n")


def delete_task(tasks):
    if not tasks:
        return

    task_id = int(input("Enter task ID to delete task : ").strip())

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"🗑️ Task {task_id} deleted. \n")
            return

    print(f"⚠️ No task found with ID {task_id}. \n")


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
    print("🗒️ Welcome to your Task Manager! \n")

    while True:
        show_menu()
        choice = input("Choose an option (1-5) : ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye")
            break
        else:
            print("⚠️Invalid choice. Please pick 1-5. \n")

        save_tasks(tasks)


if __name__ == "__main__":
    main()
