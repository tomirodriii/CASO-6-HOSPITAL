import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="6hospi"
    )
    
"""
Pacientes
0  id
1  dni
2  nombre
3  apellido
4  nacimiento
5  sexo
6  telefono
7  admisión
8  estado
9  direccion
10 email
11 grupo_sanguineo
12 contacto_emergencia
13 telefono_emergencia
14 obra_social
15 numero_afiliado
"""