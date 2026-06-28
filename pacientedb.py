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
        SELECT id_paciente, dni, nombre, apellido, fecha_nacimiento, sexo, telefono, fecha_admisión, estado FROM pacientes
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def add_paciente(nombre, apellido, dni, fecha_nacimiento, sexo, telefono,):
    
    connection = conectar ()
    cursor = connection.cursor()
    
    pdata = """INSERT INTO pacientes (nombre, apellido, dni, fecha_nacimiento, sexo, telefono, fecha_admisión, estado) 
    VALUES (%s, %s, %s, %s, %s, %s, CURDATE(), "Activo")"""
    
    valuen = (nombre, apellido, dni, fecha_nacimiento, sexo, telefono)
    
    cursor.execute(pdata,valuen)
    connection.commit()
    cursor.close()
    connection.close()
