import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

#selezione di tutti i campi da customers
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

#stampa
for x in myresult:
  print(x)
