'''Program code'''


def menu():
    '''Displays the list of options'''
    print("\n1. Create a new Task")
    print("2. View all Tasks")
    print("3. Mark Task Complete")
    print("4. Delete a Task\n")


class Task():
    '''This class is used to create task objects'''
    def __init__(self, task_id, task_title, task_desc=None):
        self.task_id = task_id
        self.task_title = task_title
        self.task_desc = task_desc
        self.task_status = "Task Pending"

    def __str__(self):
        return f"{self.task_id}.  {self.task_title} \t{self.task_status} \n{self.task_desc}"

    def mark_task(self):
        '''Used to mark the task completed'''
        self.task_status = "Task Completed"


class MainList():
    '''This class is used to control the list'''
    def __init__(self):
        self.lists = []

    def add_task(self, task):
        '''Used to add the task to the list'''
        self.lists.append(task)

    def view_task(self):
        '''Used to view the list of tasks'''
        for task in self.lists:
            print(task)
        print("")

    def complete_task(self, tid):
        '''Used to mark tasks complete'''
        for task in self.lists:
            if task.task_id == tid:
                task.mark_task()

    def del_task(self, task_id):
        '''Used to remove tasks'''
        for task in self.lists:
            if task.task_id == task_id:
                self.lists.remove(task)

# initialize the list
main_list = MainList()

while True:
    menu()

    choice = int(input("Enter what you'd like to do: "))

    if choice == 1:
        tag = int(input("Enter the Task id: "))
        title = input("Enter the title: ")
        desc = input("Enter the description of the task: ")
        temp_task = Task(tag, title, desc)
        main_list.add_task(temp_task)

    elif choice == 2:
        main_list.view_task()

    elif choice == 3:
        t_id = int(input("Enter the task id: "))
        main_list.complete_task(t_id)

    elif choice == 4:
        t_id = int(input("Enter the task id: "))
        main_list.del_task(t_id)

    else:
        break
