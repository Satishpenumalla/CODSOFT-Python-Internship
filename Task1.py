# Define a class for tasks
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

# Function to display menu options
def display_menu():
    print("Menu:")
    print("1. Add a task")
    print("2. View your tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a task to the list
def add_task():
    description = input("Enter the task description: ")
    tasks.append(Task(description))
    print("Task added successfully.")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.description} - {status}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[index].completed = True
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task number.")

# Function to delete a task from the list
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        del tasks[index]
        print("Task deleted.")
    except IndexError:
        print("Invalid task number.")

# Main function to run the application
def main():
    global tasks
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
