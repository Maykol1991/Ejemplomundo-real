import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_elemento():
    elemento = entrada_texto.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un elemento:")
etiqueta.pack(pady=10)

# Crear campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=10)

# Crear botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Crear la lista para mostrar los elementos agregados
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Crear botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()