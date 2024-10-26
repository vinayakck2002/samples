for i in range (0,4):
    for j  in range (0,4-i-1):
        print(" ",end=" ")
    for j in range (0,1+i):
        print("*",end=" ")
    print()