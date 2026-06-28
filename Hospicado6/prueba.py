import mysql.connector

def conectar():
    Bağlantı = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="6hospi"
    )
    return Bağlantı