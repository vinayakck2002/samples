import sqlite3
con=sqlite3.connect('user.db')
limit=int(input("Enter the limit: "))
for i in range(limit):
    id=int(input("Enter the id: "))
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phno=int(input("Enter your number: "))
    con.execute('insert into u_details(user_id,user_nme,user_email,user_phno)values(?,?,?,?)',(id,name,email,phno))
con.commit()
    