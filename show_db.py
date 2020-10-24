import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


print('connected')

mycursor.exectue(" SHOW DATABASES ")

for db in mycursor: #showing all the databases in your Database 
     print(db)
