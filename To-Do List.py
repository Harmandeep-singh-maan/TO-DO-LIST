Tasks = []

while True:
    print ("please select an option")
    print ("1. Add task")
    print ("2. veiw tasks")
    print ("3. remove the task")
    print ("4. exit")
    choice = int(input("select any option(1-4):"))
    #add tasks
    if choice == 1:
        task = input("enter the task:")
        Tasks.append(task)
    # veiw tasks
    elif choice == 2:
        print ("\nyour tasks")
        if len(Tasks) ==  0:
            print ("no tasks are assigned")
        else:
            for i,tasks in enumerate(Tasks,1):
                print (f"{i}.{tasks}") 
    #remove task
    elif choice == 3:
        print ("\nwhich task to remove")
        if len(Tasks) == 0:
            print("\nno task is there to remove")
            continue
        else:
            for i, tasks in enumerate(Tasks, 1):
                print (f'{i}.{tasks}')
            num = int(input("enter the number:"))
            if num > len(Tasks) or num <= 0:
                print ("enter valid number")
            else:
                removed = Tasks.pop(num-1)
                print (f"task removed:{removed}")
    #exit
    elif choice == 4:
        print ("goodbye")
        break
    else:
        print ("\nenter valid option (1-4)")