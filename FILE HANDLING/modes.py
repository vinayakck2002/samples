#MODES ARE 4 TYPE
#create --> x
#write --> w
#Append --> a
#Read --> r

#syntax: variable=open("filename","mode_name")
try:
    f=open("file.txt","x")
except:
    pass
#---------------------------------------------#
f=open("file.txt","w")
f.write("helo")
# f.write("welcome back")