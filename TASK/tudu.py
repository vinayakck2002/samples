try:
    f=open("samples/TASK/tudu.txt","a")
except:
    pass
l=[]
while True:
    print("1.Add task\n2.view task\n3.delete task\n4.Exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        task=input("Enter your task: ")
        l.append(task)
        f.write(str(l))
        print(l)
    elif choice==2:
       f = open("samples/TASK/tudu.txt", "r")
       print(f.read())
    elif choice==3:
        l.remove(input("enter the name to delete: "))
    elif choice==4:
        break
    else:
        print("invalid task")




