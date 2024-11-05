# map(function,itreble)
l=[1,2,3,4]
res=map(lambda a:a*a,l)
print(list(res))

#---------------OR-----------------#

# l=[1,2,3,4]
# res=list(map(lambda a:a*a,l))
# print(res)

l=[1,2,3,4]
def square(x):
    return x*x

res=list(map(square,l))
print(res)