try:
    f=open('newfile','x')
except:
    pass
limit=int(input("Enter a no.of student :"))
f=open('newfile','w')
for i in range(limit):
    name=(input("enter the name :"))
    f.write(name+'\n')