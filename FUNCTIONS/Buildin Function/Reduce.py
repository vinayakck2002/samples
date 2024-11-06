from functools import reduce
l=[1,2,3,4,5,6,7,8]
res=reduce(lambda x,y:x+y,l)
print(res)

# l=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x%3==0
# res=list(filter(even,l))
# print(res)

# l=[1,2,3,4,5,6]
# def 