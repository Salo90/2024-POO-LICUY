import tkinter as tk
from tkinter import messagebox


# Clase principal que maneja la aplicación de gestión de tareas
class TaskManagerApp:
    def __init__(self, root):
        # Inicialización de la ventana principal
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana
        self.root.geometry("400x400")  # Dimensiones de la ventana

        # Lista de tareas (almacena las tareas con su estado)
        self.tasks = []

        # Crear los componentes gráficos (widgets)
        self.create_widgets()

        # Asignación de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Enter para agregar tarea
        self.root.bind('<c>', lambda event: self.complete_task())  # 'C' para completar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Delete para eliminar tarea
        self.root.bind('<d>', lambda event: self.delete_task())  # 'D' para eliminar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Escape para cerrar la aplicación

    # Función para crear los componentes gráficos
    def create_widgets(self):
        # Campo de entrada para escribir la tarea
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)  # Se añade con un pequeño margen vertical

        # Botón para añadir una nueva tarea
        add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.pack(pady=5)  # Se añade con un pequeño margen vertical

        # Botón para marcar una tarea como completada
        complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        complete_button.pack(pady=5)

        # Botón para eliminar la tarea seleccionada
        delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

    # Función para añadir una nueva tarea
    def add_task(self):
        task = self.task_entry.get().strip()  # Obtener texto del campo de entrada y eliminar espacios
        if task:
            # Añadir la tarea a la lista con el estado "no completada"
            self.tasks.append({"text": task, "completed": False})
            # Actualizar la lista visual
            self.update_task_list()
            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)
        else:
            # Mostrar advertencia si el campo de entrada está vacío
            messagebox.showwarning("Entrada Vacía", "No se puede añadir una tarea vacía.")

    # Función para marcar la tarea seleccionada como completada/no completada
    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:
            task_index = selected_task_index[0]  # Convertir a índice de lista
            # Alternar el estado de completado de la tarea
            self.tasks[task_index]["completed"] = not self.tasks[task_index]["completed"]
            # Actualizar la lista visual
            self.update_task_list()
        else:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Selecciona una Tarea", "Debes seleccionar una tarea para marcarla como completada.")

    # Función para eliminar la tarea seleccionada
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:
            task_index = selected_task_index[0]  # Convertir a índice de lista
            del self.tasks[task_index]  # Eliminar la tarea de la lista
            self.update_task_list()  # Actualizar la lista visual
        else:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Selecciona una Tarea", "Debes seleccionar una tarea para eliminarla.")

    # Función para actualizar la lista visual de tareas
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista visual
        for task in self.tasks:
            task_text = task["text"]  # Obtener el texto de la tarea
            if task["completed"]:  # Si la tarea está completada, añadir "(Completada)" al texto
                task_text += " (Completada)"
            self.task_listbox.insert(tk.END, task_text)  # Insertar la tarea actualizada en la lista


# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManagerApp(root)  # Inicializar la aplicación con la ventana principal
    root.mainloop()  # Iniciar el bucle principal de Tkinter para la interfaz gráfica
