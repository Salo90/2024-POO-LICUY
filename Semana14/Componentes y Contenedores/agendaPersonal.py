import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitas instalar `tkcalendar` usando pip

# Función para agregar un evento a la lista
def agregar_evento():
    fecha = date_picker.get()
    hora = combobox_hora.get()
    descripcion = entry_descripcion.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")
        return

    # Agrega el evento al Treeview
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpia los campos de entrada
    combobox_hora.set('')
    entry_descripcion.delete(0, tk.END)

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
        if respuesta:
            for item in seleccionado:
                tree.delete(item)
    else:
        messagebox.showwarning("Sin selección", "Por favor, selecciona un evento para eliminar.")

# Función para salir de la aplicación
def salir():
    root.quit()

# Funciones para el efecto hover
def on_enter(event):
    event.widget.config(bg="#5DADE2")  # Color al pasar el mouse (azul claro)

def on_leave(event):
    event.widget.config(bg="#3498DB")  # Color original (azul)

def on_enter_rojo(event):
    event.widget.config(bg="#FF7F7F")  # Color al pasar el mouse (rojo claro)

def on_leave_rojo(event):
    event.widget.config(bg="#E74C3C")  # Color original (rojo)

def on_enter_gris(event):
    event.widget.config(bg="#D3D3D3")  # Color al pasar el mouse (gris claro)

def on_leave_gris(event):
    event.widget.config(bg="#A9A9A9")  # Color original (gris oscuro)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# Frame superior: Entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=5, pady=5)

# DatePicker para la selección de fecha
date_picker = DateEntry(frame_entrada, width=15, background='darkblue', foreground='white', borderwidth=2, year=2024)
date_picker.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora:")
label_hora.grid(row=1, column=0, padx=5, pady=5)

# Combobox para la selección de hora
horas = [f"{h:02}:00" for h in range(24)]  # Lista de horas en formato 24 horas
combobox_hora = ttk.Combobox(frame_entrada, values=horas, state="readonly", width=18)
combobox_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)

entry_descripcion = tk.Entry(frame_entrada, width=40)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame central: TreeView para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Configuración del Treeview
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.column("Fecha", width=100, anchor="center")
tree.column("Hora", width=100, anchor="center")
tree.column("Descripción", width=300, anchor="w")

tree.pack()

# Frame inferior: Botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="#0000FF", fg="white")
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="#FF0000", fg="white")
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir, bg="#A9A9A9", fg="white")
btn_salir.grid(row=0, column=2, padx=10)

# Aplicar el efecto hover a los botones
btn_agregar.bind("<Enter>", on_enter)
btn_agregar.bind("<Leave>", on_leave)

btn_eliminar.bind("<Enter>", on_enter_rojo)
btn_eliminar.bind("<Leave>", on_leave_rojo)

btn_salir.bind("<Enter>", on_enter_gris)
btn_salir.bind("<Leave>", on_leave_gris)

# Iniciar el bucle principal
root.mainloop()
