s=int(input("Enter a starting number:"))
e=int(input("Enter a ending number"))
i=0
for i in range(s,e,-1):
    if(i%2==0):
        print(i)
    