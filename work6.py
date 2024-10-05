a=int(input("enter your first num:"))
b=int(input("enter your second num:"))
print(""" 1.addition 
          2.subraction 
          3.multiplication
          4.division
          5.modules
          6.floor division 
          7.exponent """)
x=int(input("Enter your choice:"))
if(x==1):
    print(a+b)
elif(x==2):
    print(a-b)
elif(x==3):
    print(a*b)
elif(x==4):
    print(a/b)
elif(x==5):
    print(a%b)
elif(x==6):
    print(a//b)
elif(x==7):
    print(a**b)
else:
    print("not found")

        
    

