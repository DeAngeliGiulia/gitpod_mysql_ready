import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

def animali_peso2():
    mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2.0")
    result = mycursor.fetchall()
    for Animali in result:
        print(Animali)

animali_peso2()