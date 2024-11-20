import re
email=input("Enter the your Email")
check="[a-z]+[0-9]+[@]+[gmail]+[.]+[com]"
if re.search(email,check):
    print("okey")
else:
    print("Not Okey")
