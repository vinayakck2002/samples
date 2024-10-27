#TO PRINT ABC DEF GHI 3ROW AND 3 COLUMN
alpha=65
for i in range (3):
    for j in range(3):
        print(chr(alpha),end=" ")
        alpha=alpha+1
    print()