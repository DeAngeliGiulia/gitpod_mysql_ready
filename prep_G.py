import mysql.connector
import prep_C

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

def inserimento_animale():
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

def eliminare_animale():
    id_da_eliminare = input("Inserisci l'id dell'animale da eliminare: ")
    mycursor = mydb.cursor()
    mycursor.execute('DELETE FROM animali WHERE id = ?', (id_da_eliminare,))
    mydb.commit()
    mydb.close()
def modifica_animale():
    id_da_modificare = input("Inserisci l'id dell'animale da modificare: ")
    mycursor = mydb.cursor()

    Nome_Proprio = input("Nuovo Nome Proprio: ")
    Razza = input("Nuova Razza: ")
    Peso = float(input("Nuovo Peso (in kg): "))
    Eta = int(input("Nuova Età (in anni): "))

    sql = "UPDATE Mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE id = %s"
    val = (Nome_Proprio, Razza, Peso, Eta, id_animale)
    cursor.execute(sql, val)
    mydb.commit()
    print("Animale modificato con successo.")
    mydb.close()


scelta = input("Premi 1 per inserire un nuovo animale\nPremi 2 per visualizzare tutti gli animali\nPremi 3 per eliminare un animale\nPremi 4 per modificare un animale")

match scelta:
    case "1":
        inserimento_animale()
    case "2":
        prep_C.get_Mammiferi()
    case "3":
        eliminare_animale()
    case "4":
        modifica_animale()
    case _:
        print("Opzione non valida")
