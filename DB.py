import mysql.connector

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host="3306",
    user="root",
    password="",
    database="sge"
)

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * From empleado")

# Obtener los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
