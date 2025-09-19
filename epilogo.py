import tkinter as tk

def mostrar_epilogo(callback_inicio):
    epilogo_window = tk.Tk()
    epilogo_window.title("Sentencia Binaria")

    epilogo_texto = """
    En un mundo donde cada decisión deja huella, vos sos el juez invisible.
    No hay respuestas correctas, solo consecuencias.
    Tu recorrido será registrado, no para juzgarte... sino para entenderte.

    Bienvenido a *Sentencia Binaria*.
    """

    tk.Label(epilogo_window, text=epilogo_texto, wraplength=400, justify="left").pack(pady=20)
    tk.Button(epilogo_window, text="Comenzar", command=lambda: [epilogo_window.destroy(), callback_inicio()]).pack(pady=10)

    epilogo_window.mainloop()
