import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="chinook"
)

mycursor = mydb.cursor();
mycursor.execute("Select * from artist limit 6")

# print(mycursor.fetchall())