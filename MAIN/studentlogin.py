student_Details={}
while(True):
    print("1.add student details\n2.delete student details\n3.search student details\n4.show all student details\n5.exit")
    c=int(input("Enter your choice:"))

    if(c==1):
        adno=int(input("Enter your admission number:"))
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        course=input("Enter your course:")
        student_Details[adno]={"name":name, "age":age,"course":course}
        print("added successfully")
    elif(c==2):
        student_Details=student_Details-[adno]
        print("delete successfully")
    elif(c==3):
        adno=int(input("Enter your admission number:"))
        print(student_Details[adno])
    elif(c==4):
        print(student_Details)
    elif(c==5):
        break
    else:
        print("invalid")


        



