n=int(input("Enter the limit of students :"))
s=[]
for i in range(n):
    s_name=input("Enter a name :")
    s_age=int(input("Enter a age :"))
    s_place=input("Enter a place :")
    s.append({"name":s_name,"age":s_age,"place":s_place})
    print(s)

    