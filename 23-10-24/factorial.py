# find the factorial of a number
a=int(input("Enter a number:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)