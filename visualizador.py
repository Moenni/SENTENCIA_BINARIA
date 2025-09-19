import tkinter as tk
import json

def mostrar_decisiones(decisiones):
    ventana=tk.Tk
    ventana.title("Registro de Decisiones")
    
    for d in decisiones:
        texto = f"{d['momento']} - {d['dilema']}\nElegiste: {d['elección']} | Impacto: {d['impacto']}\n"
        tk.Label(ventana,text=texto,wraplength=400, justify="left").pack(pady=5)
        
    tk.Button(ventana, text="Guardar",command=lambda: guardar(decisiones)).pack(pady=10)
    ventana.mainloop()
def guardar(decisiones):
    with open("registro_decisiones,json","w")as archivo:
        json.dump(decisiones,archivo,indent=4)