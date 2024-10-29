import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

#crazione di un nuovo database
mycursor.execute("CREATE DATABASE mydatabase")

