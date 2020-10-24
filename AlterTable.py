# Editing the database in Tables
import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()



mycursor.execute("ALTER TABLE movies ADD COLUME lang VARCHAR(30) NOT NULL") #Create table with varchar 30
mycursor.execute("ALTER TABLE movies CHANGE COLUME lang VARCHAR(50) NOT NULL") #change and increase  table with varchar from 30 to 50

myconn.commit() #Always add it to your code 




