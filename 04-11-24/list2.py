#To print largest string in the list 
l=["apple","kiwi","orange","dfjjuhjujnhu"]
lar=l[0]
for i in l:
    if len(i)>len(lar):
        lar=i
print(lar)
