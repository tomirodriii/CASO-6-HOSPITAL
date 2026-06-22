import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="6hospi"
    )


def get_patient():
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_paciente, dni, nombre, apellido, fecha_nacimiento, sexo, telefono, estado FROM pacientes
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
