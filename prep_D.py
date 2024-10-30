import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

animali = []

for i in range(5):
    Nome_Proprio = input("Inserisci il nome dell'animale: ")
    Razza = input("Inserisci la razza dell'animale: ")
    Peso = float(input("Inserisci il peso (in kg) dell'animale: "))
    Eta = int(input("Inserisci l'età (in anni) dell'animale: "))
    

