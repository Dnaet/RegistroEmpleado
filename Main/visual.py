import tkinter as tk
from tkinter import messagebox

def ventana_agregar_empleado():
    ventana = tk.Tk()
    ventana.title("Agregar Empleado")

    tk.Label(ventana, text="Nombre").pack()
    nombre = tk.Entry(ventana)
    nombre.pack()

    tk.Label(ventana, text="Dirección").pack()
    direccion = tk.Entry(ventana)
    direccion.pack()

    tk.Label(ventana, text="Teléfono").pack()
    telefono = tk.Entry(ventana)
    telefono.pack()

    tk.Label(ventana, text="Correo").pack()
    correo = tk.Entry(ventana)
    correo.pack()

    tk.Label(ventana, text="Fecha de Inicio").pack()
    fecha_inicio = tk.Entry(ventana)
    fecha_inicio.pack()

    tk.Label(ventana, text="Salario").pack()
    salario = tk.Entry(ventana)
    salario.pack()

    def guardar_empleado():
        con = conectar_bd()
        emp = Empleado(nombre.get(), direccion.get(), telefono.get(), correo.get(), fecha_inicio.get(), float(salario.get()))
        Empleado.agregar_empleado(con, emp)
        cerrar_bd(con)
        messagebox.showinfo("Éxito", "Empleado agregado exitosamente")

    tk.Button(ventana, text="Guardar", command=guardar_empleado).pack()
    ventana.mainloop()
