def add(a,b):
    sum=a+b
    return sum

def subract(a,b):
    sum=a-b
    return sum

def multiply(a,b):
    sum=a*b
    return sum

def divide(a,b):
    sum=a/b
    return sum

while True:
     a=int(input("Enter a number :"))
     b=int(input("Enter a number :"))
     print("1.Addition\n2.subraction\n3.multiplication\n4.division")
     choice=int(input("Enter your choice :"))
     
     if(choice==1):
         print(add(a,b))
  





