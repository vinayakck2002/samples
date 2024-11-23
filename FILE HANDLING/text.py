f=open('samples/FILE HANDLING/text.txt','r')
# a=f.read()
# print(a)
# b=f.read()
# print(b)

# a=f.readline().strip()
# print(a)

# a=f.readline(4).strip()
# print(a)

# a=f.readlines()
# print(len(a))#length of lines in text files 


#---------------------------------------------------------------------------------------------#
# a=f.readlines()
# f.seek(0)#seek method use the cursor position is start with 0 
# for i in range(len(a)):
    # b=f.readline().strip()
#     print(b[::-1])#reverse the all lines

#---------------------------------------------------------------------------------------------#
a=f.readlines()
f.seek(0)
letter=0
number=0
capital=0
small=0
for i in range(len(a)):
    b=f.readline().strip()
    # print(b)
    for j in b:
        if j!=" ":
            letter=letter+1
        if j.isdigit():
            number+=1
        if j.isupper():
            capital+=1
        if j.islower():
            small+=1
print('capital is =',capital,'small letter is =',small)           
# print(number)#how many digit in the text file
# print(letter-number)

