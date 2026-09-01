"""
Simple To-Do List App
Run this with: python3 todo_app.py
"""

tasks = []


def add_task(tasks, title):
    tasks.append({'title': title, 'done': False})
    print('Added:', title)


def show_tasks(tasks):
    if len(tasks) == 0:
        print('No tasks yet!')
        return
    for i in range(len(tasks)):
        status = 'X' if tasks[i]['done'] else ' '
        print(f"{i}. [{status}] {tasks[i]['title']}")


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print('Invalid task number.')
        return
    tasks[index]['done'] = True
    print('Marked as done:', tasks[index]['title'])


def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print('Invalid task number.')
        return
    removed = tasks.pop(index)
    print('Removed:', removed['title'])


def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
            else:
                print("Task title cannot be empty.")
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            show_tasks(tasks)
            try:
                index = int(input("Task number to mark done: "))
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            show_tasks(tasks)
            try:
                index = int(input("Task number to remove: "))
                remove_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please pick 1-5.")


if __name__ == "__main__":
    main()
