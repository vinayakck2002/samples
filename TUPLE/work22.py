#TUPLE

# ADD ONE VARIABLE  IN TUPLE LIST
t=(1,2,3,4)
l=list(t)
l.append(5)
t=tuple(l)
print(t)                                                               

#ADD MULTIPLE VARIABLE IN TUPLE LIST
t=(1,2,3,4)
l=list(t)
l.extend([5,6,7])
t=tuple(l)
print(t)  
