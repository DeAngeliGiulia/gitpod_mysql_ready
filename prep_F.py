"""
import mysql.connector
import prep_C

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

animali = []

for i in range input('inserisci il numero di animali da inserire'):
    Nome_Proprio = input("Inserisci il nome dell'animale: ")
    Razza = input("Inserisci la razza dell'animale: ")
    Peso = float(input("Inserisci il peso (in kg) dell'animale: "))
    Eta = int(input("Inserisci l'età (in anni) dell'animale: "))
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (Nome_Proprio, Razza, Peso, Eta)
    mycursor.execute(sql, val)
    i = 1 +1

mydb.commit()

print(mycursor.rowcount, "Animali inseriti.")
if i == 5:
  prep_C.get_Mammiferi
"""

