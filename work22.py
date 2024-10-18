#TUPLE

#CHANGE ONE VARIABLE ADD IN TUPLE LIST
t=(1,2,3,4)
l=list(t)
l.append(5)
t=tuple(l)
print(t)

#CHANGE MORE THAN VARIABLE ADD IN TUPLE LIST
t=(1,2,3,4)
l=list(t)
l.extend(5,6,7)
t=tuple(l)
print(t)