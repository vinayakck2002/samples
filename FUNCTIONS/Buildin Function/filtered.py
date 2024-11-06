l=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,l))
print(even)

#-----------------OR---------------------

l=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x%2==0
res=list(filter(even,l))
print(res)

#------------------------------------------
#divisible
l=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x%3==0
res=list(filter(even,l))
print(res)



l=(1,2,3,4,5,6)
sum=0
for i in l:
    sum=sum+i
print(sum)
