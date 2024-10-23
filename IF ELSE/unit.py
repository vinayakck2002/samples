unit=int(input("Enter the unit:"))
if(unit<=100):
    print("no charge")
elif(unit<=200):
    unit=200-100
    cost=unit*5
    print(cost)
elif(unit>200):
    unit=unit-200
    cost=(unit*10)+500
    print(cost)
else:
    print("Invalid")
    
  