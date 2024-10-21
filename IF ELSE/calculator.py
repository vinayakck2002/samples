num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
print("1.Addition\n2.subraction\n3.multiplication\n4.division")
check=int(input("choose your selection"))
if(check==1):
    print(num1+num2)
elif(check==2):
    print(num1-num2)
elif(check==3):
    print(num1*num2)
elif(check==4):
    print(num1/num2)
else:
    print("Invalid")