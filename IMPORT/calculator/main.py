#Calulator to use import function

from add import add 
from sub import sub
from mul import mul
from div import div
from number import number
while True:
    print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        a,b=number()
        add(a,b)
    elif choice==2:
        a,b=number()
        sub(a,b)
    elif choice==3:
        a,b=number()
        mul(a,b)
    elif choice==4:
        a,b=number()
        div(a,b)
    elif choice==5:
        break
    else:
        print("invalid")


    