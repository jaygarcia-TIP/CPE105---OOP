# Author: Jay Garcia - BSCPE CPE1S1
# Created: 05/11/2024
# Clever cloud - Database Python program (Online Database) - Assignment

import mysql.connector

mydb = mysql.connector.connect(
    host = "bhcjvnvbg1h0mctnkjpq-mysql.services.clever-cloud.com",
    user = "uy5ywmtde9y5lvf4",
    password = "xc9xkIXG0clQNYJ5dsWv",
    database = "bhcjvnvbg1h0mctnkjpq"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM table_students")
fetched_Data = mycursor.fetchall()

for results in fetched_Data:
    print(results)
