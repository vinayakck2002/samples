a=int(input("Enter a value: "))

try:
    f=open("samples/FILE HANDLING/mul.txt","x")#create a text file stored in a f variable
except:
    pass
f=open('samples/FILE HANDLING/mul.txt','w')
for i in range(1,11):
    print(i,"*",a,"=",i*a)
    f.write(str(i)+"*"+str(a)+"="+str(i*a)+"\n")


