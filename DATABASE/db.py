import sqlite3
con=sqlite3.connect('userr.db')
try:
    con.execute('create Table u_details(user_id int,user_nme text,user_email text,user_phno int)')
except:
    pass
# con.execute('insert into u_details(user_id,user_nme,user_email,user_phno)values(4,"rocky","rocky@gmail.com",1234560000)')
# con.execute('delete from u_details where user_id=4')
# con.execute('update u_details set user_phno=1234560000 where user_id=4')
# data=con.execute('select*from u_details')
# # data=con.execute('select*from u_details where user_id=1')
# for i in data:
#     print("{:<10} {:<10} {:<20} {:<20}".format(i[0],i[1],i[2],i[3]))
#-----------------------------------------------------------------------------#


# data=con.execute('select count(*) from u_details')
# for i in data:
#     print(i)


#-----------------------------------------------------------------------------#

# data=con.execute('select sum(user_id) from u_details')
# for i in data:
#     print(i)
    
#------------------------------------------------------------------------------#

# data=con.execute('select avg(user_id) from u_details')
# for i in data:
#     print(i)
    
#-------------------------------------------------------------------------------#

# data=con.execute('select min(user_id) from u_details')
# for i in data:
#     print(i)
    
#------------------------------------------------------------------------------#

data=con.execute('select max(user_id) from u_details')
for i in data:
    print(i)

# con.commit()