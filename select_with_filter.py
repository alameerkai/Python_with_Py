import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


mycursor.execute("  SELECT * FROM movies WHERE name='COCO' ") # here you can get back all data from the database

resutlt = mycursor.fetchone() # here your can catch one the data with the name of vriable 


print(resutlt) # sow the data you want
