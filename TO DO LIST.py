class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"title": task, "completed": False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']} - {status}")

    def update_task(self, task_number, completed):
        try:
            task = self.tasks[task_number - 1]
            task["completed"] = completed
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Quit")
            choice = input("Choose an option: ")

            if choice == "1":
                task = input("Enter task title: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = int(input("Enter task number: "))
                completed = input("Mark as completed? (y/n): ")
                self.update_task(task_number, completed.lower() == "y")
            elif choice == "4":
                task_number = int(input("Enter task number: "))
                self.delete_task(task_number)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()