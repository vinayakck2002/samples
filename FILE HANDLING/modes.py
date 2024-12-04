#MODES ARE 4 TYPE
#create --> x
#Read --> r
#write --> w
#Append --> a

#syntax: variable=open("filename","mode_name")

# try:
#     f=open("samples/FILE HANDLING/demo.txt","x")#create a text file stored in a f variable
# except:
#     pass
# f=open('samples/FILE HANDLING/demo.txt','w')#
# f.write('Welcome back another folder')

# f=open("file.txt","w")
# f.write("helo")
# # f.write("welcome back")

#---------------------------------------------#
f=open("samples/FILE HANDLING/demo.txt","a")
# f.write('data')

a='happy'
b='new'
c='year'
f.write(a+b+c)#multiple variables  adding use +

d=[10,11]
f.write(str(d))#we dont have add directly interger value ,we can convert to string then can add   




