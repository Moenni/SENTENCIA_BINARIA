# estilo.py
def aplicar_estilo(ventana):
    ventana.configure(bg="#1e1e1e")

def estilo_label(texto, ventana):
    import tkinter as tk
    return tk.Label(ventana, text=texto, fg="white", bg="#1e1e1e", font=("Helvetica", 12))
