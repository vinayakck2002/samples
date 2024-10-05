a=int(input("enter your first num:"))
b=int(input("enter your second num:"))
c=int(input("enter your third num:"))
if(a>b):
    if(a>c):
        print(a,"is larger")
    else:
        print(c,"is larger")
else:
    if(b>c):
        print(b,"is larger")
    else:
        print(c,"is larger")
        
