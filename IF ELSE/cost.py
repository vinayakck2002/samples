cost=int(input("Enter the cost of bike:"))
if(cost>100000):
    print(cost*15/100)
elif(cost>50000 and cost<=100000):
    print(cost*10/100)
elif(cost<50000):
    print(cost*5/100)
else:
    print("Invalid")
    