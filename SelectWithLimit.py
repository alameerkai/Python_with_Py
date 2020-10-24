import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


mycursor.execute("SELECT * FROM movies LIMT 4 " ) #Here you can show how many data you want to show in the Display 
mycursor.execute("SELECT * FROM movies LIMT 4 OFFSET 5 " ) #Here you can show how many data you want to show in the Display (( form to )) 


resutlt = mycursor.fetchall() # here your can catch all the data with the name of vriable 


for movie in resutlt:
    print(movie)


