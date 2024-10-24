# #To print user define even number using for loop  
  
s=int(input("Enter a starting value:"))
e=int(input("Enter a ending value:"))
i=0
for i in range(s,e):
    if(i%2==0):
        print(i)
        
# #To Reverse print user define even number using for loop 

s=int(input("Enter a starting value:"))
e=int(input("Enter a ending value:"))
i=0
for i in range(e,s,-1):
    if(i%2==0):
        print(i)