# sum of even natural odd number
l=int(input("Enter the limit:"))
nsum=0
esum=0
osum=0
i=1
while(i<=l):
    nsum=nsum+i
    if(i%2==0):
        esum=esum+i
    elif(i%2==1):
        osum=osum+i
    i=i+1
print(nsum,"is the sum of natural number")
print(esum,"is the sum of even number")
print(osum," is the sum of odd number")



    
    