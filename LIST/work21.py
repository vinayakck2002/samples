# remove duplicate values from the list
list=["Hai","helo","Hai"]
L=[]
for i in list:
    if i not in L:
        L.append(i)
print(L)