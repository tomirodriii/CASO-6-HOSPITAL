from prueba import conectar

try:
    connection = conectar()
    print("¡¡¡Conexión extosa!!!")
    connection.close()
    
except Exception as e:
    print("Error al conectar bd.", e)
