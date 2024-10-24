# #To print 1 to 10 odd number using for loop
s=int(input("Enter a starting value:"))
e=int(input("Enter a ending value:"))
for i in range(s,e): 
    if(i%2==1):
        print(i)
        
# #To print Reverse 1 to 10 odd number using for loop
s=int(input("Enter a starting value:"))
e=int(input("Enter a ending value:"))
for i in range(e,s,-1): 
    if(i%2==1):
        print(i)
    
    