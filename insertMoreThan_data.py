import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YES"
)

mycursor = myconn.cursor()


print('connected')

mycursor.exectue()

sql = "INSERT INTO movies (name , plot ) VALUES(%s , %s)" # this is way make user add data
data = [("Now You See Me" , "Action"),
        ("COCO", "Anime"),
        ("more than one ","Action"),
        ("Demo","Demo"),
        ("Demo1","Demo1")
        
        ]

mycursor.executemany(sql , data) # here with (executemany) you can add more than data in the same order

myconn.commit() # so important to add the data and save it in the database 

print("Done")
print(mycursor.lastrowid) # show the id of the last item in your database

