import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


mycursor.execute("SELECT * FROM movies WHERE name like '%COCO%' ") # here you can get back all data from the database with this name or like it 

resutlt = mycursor.fetchall() # here your can catch all the data with the name of vriable 


print(resutlt) # show the data you want


