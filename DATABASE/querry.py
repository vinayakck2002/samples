import sqlite3
con=sqlite3.connect('user.db')
try:
    con.execute('create Table u_details(user_id int,user_nme text,user_email text,user_phno int)')
except:
    pass
con.execute('insert into u_details values(123,"abhi","abhi@gmail.com",9495334256)')
con.commit()