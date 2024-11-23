import sqlite3
con=sqlite3.connect('samples/DATABASE/std.db')
# limit=int(input("Enter the limit: "))
try:
    con.execute('create Table std_d(adm_no int,user_nme text,user_email text,total_mark int)')
except:
    pass
# for i in range(limit):
#     id=int(input("Enter the id: "))
#     name=input("Enter your name: ")
#     email=input("Enter your email: ")
#     total_mark=int(input("Enter your mark: "))
#     con.execute('insert into std_d(adm_no,user_nme,user_email,total_mark)values(?,?,?,?)',(id,name,email,total_mark))
# con.commit()

con.execute('update std_d set user_email="richu12@gmail.com" where adm_no=4')
data=con.execute('select count(*) from std_d')
for i in data:
    print(i)
data=con.execute('select sum(adm_no) from std_d')
for i in data:
    print(i)
data=con.execute('select avg(adm_no) from std_d')
for i in data:
    print(i)
data=con.execute('select min(adm_no) from std_d')
for i in data:
    print(i)
con.commit()