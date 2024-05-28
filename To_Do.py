to_do=[]

def add_task(task):
   to_do.append(task)
   print("Task added successfully!")

def display_task():
   if to_do:
      print("Tasks:")
      for index,task in enumerate(to_do,start=1):
         print(f"{index}.{task}")
   else:
      print("No task found!")

def remove_task(removed_task):
   if removed_task in to_do:
      to_do.remove(removed_task)
      print("Task removed successfully!")
   else:
      print("Task not found")

def update_task(old_task,new_task):
   if old_task in to_do:
      index = to_do.index(old_task)
      to_do[index] = new_task
      print("Task updated successfully!")
   else:
      print("Task isn't there")


while True:
    print("\n Menu:")
    print("1.Add a task")
    print("2.Display the tasks")
    print("3.Delete a task")
    print("4.Update the task")
    print("5.Exit")
    choice=input("Enter the Choice: ")

    if choice == "1":
      task = input("enter the task: ").capitalize()
      add_task(task)

    elif choice == "2":
       display_task()

    elif choice == "3":
       removed_task = input("Enter the task to remove: ").capitalize()
       remove_task(removed_task)

    elif choice == "4":
       old_task = input("Enter the task to update: ").capitalize()
       new_task = input("Enter the new task: ").capitalize()
       update_task(old_task,new_task)

    elif choice == "5":
       print("Exiting...")
       break
    
    else:
       print("Invalid choice!")