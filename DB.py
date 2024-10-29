import mysql.connector

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_base_datos"
)

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM usuarios")

# Obtener los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
