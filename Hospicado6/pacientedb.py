from db import conectar #Abre la conexión a la base de datos de MYSQL XAMPP.

def get_patient():  # Obtener pacientes.
    connection = conectar()  # crea la conexión a la base de datos.
    cursor = connection.cursor()  # crea el cursor para ejecutar consultas.
    cursor.execute("""
        SELECT id_paciente,dni, nombre, apellido, fecha_nacimiento, sexo, telefono, fecha_admisión, estado, direccion,
    email, grupo_sanguineo, contacto_emergencia, telefono_emergencia, obra_social, numero_afiliado FROM pacientes
    """)  # ejecuta la consulta SQL para obtener los pacientes.
    data = cursor.fetchall()  # obtiene todos los registros de la consulta.
    cursor.close()  # cierra el cursor.
    connection.close()  # cierra la conexión a la base de datos.
    return data  # devuelve todos los datos de pacientes obtenidos.

def add_paciente(nombre, apellido, dni, fecha_nacimiento, sexo, telefono,):
    connection = conectar()  
    cursor = connection.cursor()  

    pdata = """INSERT INTO pacientes (nombre, apellido, dni, fecha_nacimiento, sexo, telefono, fecha_admisión, estado) 
    VALUES (%s, %s, %s, %s, %s, %s, CURDATE(), "Activo")"""  # define la consulta SQL para insertar un paciente.

    valuen = (nombre, apellido, dni, fecha_nacimiento, sexo, telefono)  # Los valores a insertar.

    cursor.execute(pdata, valuen)  # ejecuta la inserción con los valores proporcionados.
    connection.commit()  # confirma los cambios en la base de datos.
    cursor.close()
    connection.close()  # Inserta un nuevo paciente.
    
    
def update_paciente(id_paciente, nombre, apellido, dni, fecha_nacimiento, sexo, telefono): #Modificar pacientes.
    connection = conectar()  
    cursor = connection.cursor()  

    pdata = """UPDATE pacientes SET nombre=%s, apellido=%s, dni=%s, fecha_nacimiento=%s, sexo=%s, telefono=%s WHERE id_paciente=%s"""  # define la consulta SQL para actualizar un paciente mediante placeholders.

    val = (nombre, apellido, dni, fecha_nacimiento, sexo, telefono, id_paciente)  # Los valores a actualizar.

    cursor.execute(pdata, val)  # ejecuta la actualización con los valores proporcionados.
    connection.commit()  # confirma los cambios en la base de datos.
    cursor.close()
    connection.close()  # Modifica un paciente existente.
    
def get_idpaciente(id_paciente):  # Obtener paciente por ID.
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id_paciente=%s", (id_paciente,))
    patient = cursor.fetchall()
    cursor.close()
    connection.close()
    return patient #Obtiene un único paciente para cargar al formulario al editar.


def delete_paciente(id_paciente): # Eliminar paciente existente por ID.
    connection = conectar()  
    cursor = connection.cursor()  

    pdata = """DELETE FROM pacientes WHERE id_paciente=%s"""  # define la consulta SQL para eliminar un paciente mediante el id indicado.

    cursor.execute(pdata, (id_paciente,))  # ejecuta la eliminación con el id proporcionado.
    connection.commit()  # confirma los cambios en la base de datos.
    cursor.close()
    connection.close()  