import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def agregar_dato():
    dato = campo_texto.get()
    if dato:
        # Inserta los datos en la tabla
        tabla_datos.insert("", tk.END, values=(dato,))
        campo_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_datos():
    campo_texto.delete(0, tk.END)
    for item in tabla_datos.get_children():
        tabla_datos.delete(item)

def on_enter_agregar(event):
    boton_agregar.config(bg="#0604ba")  # Cambia a un azul más oscuro

def on_leave_agregar(event):
    boton_agregar.config(bg="#0050c3")  # Cambia de vuelta al azul original

def on_enter_limpiar(event):
    boton_limpiar.config(bg="#b4b4b4")  # Cambia a un color rosa claro

def on_leave_limpiar(event):
    boton_limpiar.config(bg="#F0F0F0")  # Cambia de vuelta al color gris claro

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Establecer dimensiones de la ventana
ventana.geometry("400x300")  # Ancho x Alto

# Colores de fondo
color_fondo = "#F0F0F0"  # Beige
color_boton_agregar = "#0000FF"  # Azul
color_texto_boton_agregar = "#FFFFFF"  # Blanco
color_boton_limpiar = "#F0F0F0"  # Gris claro

# Aplicar colores de fondo
ventana.config(bg=color_fondo)

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:", bg=color_fondo)
etiqueta.pack(pady=5)

# Campo de texto
campo_texto = tk.Entry(ventana, width=40)
campo_texto.pack(pady=5)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg=color_fondo)
frame_botones.pack(pady=10)

# Botón "Agregar" con efecto hover
boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_dato, bg=color_boton_agregar, fg=color_texto_boton_agregar)
boton_agregar.pack(side=tk.LEFT, padx=5)
boton_agregar.bind("<Enter>", on_enter_agregar)  # Evento al pasar el mouse
boton_agregar.bind("<Leave>", on_leave_agregar)   # Evento al salir el mouse

# Botón "Limpiar" con efecto hover
boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_datos, bg=color_boton_limpiar)
boton_limpiar.pack(side=tk.LEFT, padx=5)
boton_limpiar.bind("<Enter>", on_enter_limpiar)  # Evento al pasar el mouse
boton_limpiar.bind("<Leave>", on_leave_limpiar)   # Evento al salir el mouse

# Crear y configurar el estilo de la tabla
style = ttk.Style()
style.configure("Treeview",
                background=color_fondo,
                foreground="black",
                rowheight=25,
                fieldbackground=color_fondo,
                bordercolor="#dddddd",  # Color de borde
                borderwidth=1)          # Ancho del borde

style.configure("Treeview.Heading",
                background="#a0a0a0",
                foreground="black",
                relief="flat")  # Sin relieve en los encabezados

style.map("Treeview.Heading",
          background=[('selected', '#a0a0a0')])

# Configuración de líneas de división
style.configure("Treeview",
                highlightthickness=0,  # Sin líneas de enfoque
                bd=0,  # Sin borde alrededor de la tabla
                relief="flat")

# Tabla para mostrar los datos
tabla_datos = ttk.Treeview(ventana, columns=("Datos"), show="headings")
tabla_datos.heading("Datos", text="Datos")
tabla_datos.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
