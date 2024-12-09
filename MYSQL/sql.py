import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="vinayakck2002",
    password="vinayakck317",
    database="mydb"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create table with BIGINT for user_phno
mycursor.execute('''
CREATE TABLE IF NOT EXISTS u_details (
    user_id INT,
    user_nme TEXT,
    user_email TEXT,
    user_phno BIGINT
)
''')

# Insert data
mycursor.execute('''
INSERT INTO u_details (user_id, user_nme, user_email, user_phno)
VALUES (123, "abhi", "abhi@gmail.com", 9495334256)
''')

# Commit the changes
mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()

print("Connected and data inserted successfully!")
