import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


print('connected')

mycursor.exectue(" CREATE TABLE movies (name VARCHAR(100), polt VARCHAR(500))")

print("everything is okay")