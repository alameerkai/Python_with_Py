import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


print('connected')

mycursor.exectue("CREATE DATABASE mydb ")