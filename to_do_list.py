Tasks=[]
while True:

  print("===== TO-DO LIST =====")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Remove task")
  print("4. Exit")
  choice=int(input("Enter the Choice :- "))
  
  if choice==1:
    new_task=input("Enter Task :- ")
    Tasks.append(new_task)
    print("Task added 😊")
  elif choice==2:
    for i , Task in enumerate(Tasks,1):
          print("Task", i, "is",Task)
  elif choice==3:
     remove_choice=int(input("Enter the number of task you wanna delete "))
     Tasks.pop(remove_choice-1)
     print("Task Removed")
  elif choice==4:
     break
  else:
     print("Invalid Input ")
     print("Try again")
     