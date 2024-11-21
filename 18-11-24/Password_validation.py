import re
password=input("Enter the Password: ")
check="[a-z]+[0-9]+[@]+[.]"
if re.search(password,check):
    print("Correct")
else:
    print("Incorrect")
