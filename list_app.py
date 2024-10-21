# Create functions for each feature

taskdict = {} # Initialize task dictionary

prgrm_run = 0

def addtask():
    task = input("Please input the new task: ")
    try:
        taskdict.update({task :"Incomplete."})
        print(f"Added the task: {task}!")
    except:
        print(f"Unable to add task. Try again! :)")
    finally:
        print(("*" * 5) + "Back to Main Menu" + ( "*" * 5 ))

def rmtask():
    print
    task = input("Please input the task to be removed: ")
    try:
        taskdict.pop(task)
        print(f"Removed the task: {task}!")
    except:
        print(f"Unable to find task. Try again! :)")
    finally:
        print(("*" * 5) + "Back to Main Menu" + ( "*" * 5 ))

def mkcomp():
    task = input("Please input the completed task: ")
    try:
        taskdict.update({task:"Complete!"})
    except:
        print(f"Something went wrong. Sending you back to the Menu.")
    finally:
        print(("*" * 5) + "Back to Main Menu" + ( "*" * 5 ))

def viewtasks():
    print(f"     Your Todo List:")
    i = 0 #times to iterate
    for task, status in taskdict.items():
        i += 1
        print("    {}. {} ({})".format(i, task, status))
    print(("*" * 5) + "Back to Main Menu" + ( "*" * 5 ))

def main():
    print("Welcome to the To-Do List Application.")
    welcome_msg = '''## MAIN MENU ##

    1. Add Task
    2. View Tasks
    3. Complete Tasks
    4. Delete Task
    5. Quit
    '''

    while True: #We will change this to false when we want to program to end. Otherwise, I want it to return here: to the main menu
        print(welcome_msg)
        command = input("Please select a task using a number input.")
        try:
            command = int(command)
            if command == 1:
                print("You've selected: Add Task ")
                addtask()
            elif command == 2:
                print("You've selected: View Tasks ")
                viewtasks()
            elif command == 3:
                print("You've selected: Complete Task ")
                mkcomp()
            elif command == 4:
                print("You've selected: Delete Task")
            elif command == 5:
                print("Okay! Closing the program.")
                break #break the program
        except:
            print("Please enter an integer between 1-5 for your selection. :)")
            print(("*" * 5) + "Back to Main Menu" + ( "*" * 5 ))

#then we just call the main function

main()
