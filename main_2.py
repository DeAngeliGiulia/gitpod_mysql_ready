import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

#creazione di una tabella chiamata costumers che contiene due colonne: name e address
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
