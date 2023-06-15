import mysql.connector

def conectar():
    try:
        db = mysql.connector.connect(
            host = "172.31.88.82",
            user = "root",
            password = "1994",
            database = "livro"
            )
        print("Conectado com sucesso")
    except:
        print("ERROR")
    return db
conectar()