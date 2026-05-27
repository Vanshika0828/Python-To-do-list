tasks=[]

def add_task():
  task=input("Enter task:")
  tasks.append(task)

def show_task():
  if not tasks:
    print("No tasks")
  else:
    for i,t in enumerate(tasks,1):
        print(i,".",t)

def delete_task():
    show_task()
    if tasks:
      n=int(input("Enter number:"))
      if 1<=n<=len(tasks):
        tasks.pop(n-1)

while True:
    print("\n1.Add 2.show 3.delete 4.exit")
    ch=input("choice:")

    if ch=='1':
     add_task()
    elif ch=='2':
     show_task()
    elif ch=='3':
     delete_task()
    elif ch=='4':
     break
    else:
     print("Invalid..")
    
