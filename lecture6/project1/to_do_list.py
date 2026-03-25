def task():
    tasks = []
    print("Welcome to the app management")

    totaltask = int(input("Enter the task ="))
    for i in range(1, totaltask+1):
        task_name= input(f"Enter task {i}")
        tasks.append(task_name)
    print(f"today tasks are \n {tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-Delete\n4-View\n5-Exit/stop"))
        if operation ==1:
            add = input("enter the value =")
            tasks.append(add)
            print(f"tasks {add} has been successfully added =")
            print(f"tasks added {tasks}")
        elif operation ==2:
            update = input("Enter the value of the updated =")
            if update in tasks:
                new = input("Enter the new tasks =")
                ind = tasks.index(update)
                tasks[ind]=new
                print(f"Updated tasks {new}")
        elif operation == 3:
            delete = input("which task you want to delete =")
            if delete in tasks:
                 ind = tasks.index(delete)
                 del tasks[ind]
                 print(f"task {delete} has been deleted")
        elif operation == 4:
            view = tasks
            print(f"The total task is {view}")
        elif operation ==5:
            print("closing the program")
            break   
        else:
            print("invalid input please input between 1 to 5")          

task()                


