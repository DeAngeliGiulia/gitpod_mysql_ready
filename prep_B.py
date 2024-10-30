import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta ) VALUES (%s, %s, %s, %s)"
val = [
  ('Leo', 'Labrador Retriever', 30, 5),
  ('Miao', 'Siamese', 4, 3),
  ('Max', 'Pastore Tedesco', 35, 7),
  ('Bella', 'Golden Retriever', 28, 4),
  ('Piuma', 'Coniglio Nano', 1.5, 2),
]

mycursor.executemany(sql, val)

mydb.commit()
