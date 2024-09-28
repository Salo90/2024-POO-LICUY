import tkinter as tk
from tkinter import messagebox

# Función para añadir tareas
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")

# Función para marcar tareas como completadas
def marcar_completada():
    try:
        tarea_index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_index)
        lista_tareas.delete(tarea_index)
        lista_tareas.insert(tarea_index, tarea + " (Completada)")
    except:
        messagebox.showwarning("Selección Incorrecta", "Por favor, seleccione una tarea para marcar como completada.")

# Función para eliminar tareas
def eliminar_tarea():
    try:
        tarea_index = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_index)
    except:
        messagebox.showwarning("Selección Incorrecta", "Por favor, seleccione una tarea para eliminar.")

# Función para añadir tarea al presionar Enter
def agregar_tarea_enter(event):
    agregar_tarea()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tareas
boton_agregar = tk.Button(ventana, text="Añadir Tarea", width=20, command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=10, pady=10)

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, height=10, width=50)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tareas como completadas
boton_completar = tk.Button(ventana, text="Marcar como Completada", width=20, command=marcar_completada)
boton_completar.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tareas
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Asignar la tecla Enter para añadir tareas
ventana.bind('<Return>', agregar_tarea_enter)

# Iniciar la ventana principal
ventana.mainloop()
