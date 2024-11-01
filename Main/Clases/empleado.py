import sqlite3
from datetime import datetime

class Empleado:
    def __init__(self, nombre, direccion, telefono, correo, fecha_inicio, salario):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.salario = salario

    @staticmethod
    def agregar_empleado(con, empleado):
        cursor = con.cursor()
        cursor.execute('''
            INSERT INTO Empleado (nombre, direccion, telefono, correo, fecha_inicio, salario)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo, empleado.fecha_inicio, empleado.salario))
        con.commit()

    @staticmethod
    def obtener_empleados(con):
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Empleado")
        return cursor.fetchall()

    @staticmethod
    def actualizar_empleado(con, id_empleado, nombre, direccion, telefono, correo, fecha_inicio, salario):
        cursor = con.cursor()
        cursor.execute('''
            UPDATE Empleado SET nombre = ?, direccion = ?, telefono = ?, correo = ?, fecha_inicio = ?, salario = ?
            WHERE id_empleado = ?
        ''', (nombre, direccion, telefono, correo, fecha_inicio, salario, id_empleado))
        con.commit()

    @staticmethod
    def eliminar_empleado(con, id_empleado):
        cursor = con.cursor()
        cursor.execute("DELETE FROM Empleado WHERE id_empleado = ?", (id_empleado,))
        con.commit()
