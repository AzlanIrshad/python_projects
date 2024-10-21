task_list = []
# Add items to the list
def add(task_list):
    while True:
        task_name = input("Enter the task to add: ")
        task_list.append(task_name)
        print("current task list:", task_list)
        choice = input("Do you want to add more tasks? (y / n)")
        if choice.lower() == "n":
            break
# view if the item is in the list or not.
# If the item is not present then add it.
def view(task_list):
    task_list.sort()
    task_name = input("Enter the task to view: ")
    if task_name in task_list:
        print("task present!")
    else:
        print("task not present")
        task_list.append(task_name)
    print("updated task list:", task_list)
# Remove any item from the list
def remove(task_list):
    task_name = input("Enter the task name to remove: ")
    if task_name in task_list:
        task_list.remove(task_name)
        print("task removed:", task_name)
        print("new task list", task_list)
    else:
        print("task not there!")
        print("List Unchanged:", task_list)


add(task_list)
view(task_list)
remove(task_list)

