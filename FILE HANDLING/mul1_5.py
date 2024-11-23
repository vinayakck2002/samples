n=int(input("Enter a number: "))
f=open("samples/FILE HANDLING/mul1_5.txt","w")
for i in range (1,11):
    for j in range (1,n+1):
        # print('{:<2} x {:<2} = {:<2}'.format(i,j,i*j), end="\t")
        f.write(str(i) + "x" + str(j) + "=" + str(i*j)+ "\t")
    f.write('\n')#print for new line in text file 
    # print()
