import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


mycursor.execute("SELECT * FROM movies ORDER BY name" ) #your can sort the data whit name   #Defult is from A to Z 
mycursor.execute("SELECT * FROM movies ORDER BY name DESC" ) #your can sort the data whit name   from Z to A  

resutlt = mycursor.fetchall() # here your can catch all the data with the name of vriable 


print(resutlt) # show the data you want


