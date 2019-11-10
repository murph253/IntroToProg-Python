# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JMurphy,11.9.2019,Completed Script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
txt_file = "ToDoList.txt"  # A text file containing list items
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
lstRow = []
strChoice = ""  # A Capture the user option selection



# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

objFile = open(txt_file, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options:
    1) Show current task list.
    2) Add a new task.
    3) Remove an existing task.
    4) Save Data to File.
    5) Exit Program.
    """)
    print()
    strChoice = str(input("  Please select an option [1 to 5]:  "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Your Current task list: "'\n')
        if not lstTable:
            print("Empty!")
        else:
            print("Task:          Priority:")
            for objRow in lstTable:
                print("  ", (objRow['task']) + " ------>", (objRow['priority']))
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask_item = str(input("Enter New Task: "))
        if strTask_item not in lstTable:
            strPriority_lvl = str(input("Enter Priority Level: "))
            dictRow = {"task": strTask_item, "priority": strPriority_lvl}
            lstTable.append(dictRow)
        else:
            print(strTask_item, "already exists in task list.")
        continue

    # Step 5 - Remove an item from the list/Table
    elif strChoice.strip() == '3':
        remTask = input("Enter the 'Task' you wish to remove: ")
        remPriority = input("Enter the 'Priority' for the task you wish to remove: ")
        lstTable.remove({'task': remTask, 'priority': remPriority})
        print("Task and Priority successfully removed."'\n')
        strChoice = str(input("Would you like to make another list revision? [Y]es or [N]o: "'\n'))
        if strChoice.lower() == 'y':
            remTask = input("Enter the 'Task' you wish to remove: ")
            remPriority = input("Enter the 'Priority' for the task you wish to remove: ")
            lstTable.remove({'task': remTask, 'priority': remPriority})
        elif strChoice.lower() == 'n':
            continue
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for x in lstTable:
            objFile.write(x["task"] + "," + x["priority"] + "\n")
        objFile.close()
        print("****************All Data Saved****************")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        strChoice = str(input("Are you sure you wish to exit? [Y]es or [N]o: "))
        if strChoice.lower() == 'y':
            print("Goodbye!")
            input("Press any key to exit")
            break
        elif strChoice.lower() == 'n':
            continue
        else:
            print("Please make a valid selection of either [Y]es or [N]o!")

        continue  # and Exit the program
