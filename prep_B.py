import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (id ,Nome_Proprio, Razza, Peso, Eta ) VALUES (%s, %s, %s, %s, %s)"
val = [
  (1, 'Leo', 'Labrador Retriever', 30, 5),
  (2, 'Miao', 'Siamese', 4, 3),
  (3, 'Max', 'Pastore Tedesco', 35, 7),
  (4, 'Bella', 'Golden Retriever', 28, 4),
  (5, 'Piuma', 'Coniglio Nano', 1.5, 2),
]

mycursor.executemany(sql, val)

mydb.commit()
