import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


sql="SELECT * FROM movies WHERE name=%s" 
data = ('theRock',)  

mycursor.execute(sql,data)


resutlt = mycursor.fetchall() # here your can catch all the data with the name of vriable 


print(resutlt) # show the data you want


