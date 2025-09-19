import tkinter as tk
import json

decisiones = []

def registrar_decision(eleccion):
    decisiones.append({
        "momento": "Inicio",
        "dilema": "¿Salvar al informante o proteger tu anonimato?",
        "elección": eleccion,
        "impacto": "Confianza vs Seguridad"
    })
    mostrar_resultado()

def mostrar_dilema():
    dilema_window = tk.Tk()
    dilema_window.title("Dilema Ético")

    tk.Label(dilema_window, text="¿Salvar al informante o proteger tu anonimato?", wraplength=400).pack(pady=20)
    tk.Button(dilema_window, text="Salvar al informante", command=lambda: [dilema_window.destroy(), registrar_decision("Salvar")]).pack()
    tk.Button(dilema_window, text="Proteger anonimato", command=lambda: [dilema_window.destroy(), registrar_decision("Proteger")]).pack()

def mostrar_resultado():
    resultado_window = tk.Tk()
    resultado_window.title("Registro de Decisiones")

    for d in decisiones:
        texto = f"{d['momento']} - {d['dilema']}\nElegiste: {d['elección']} | Impacto: {d['impacto']}\n"
        tk.Label(resultado_window, text=texto, wraplength=400, justify="left").pack(pady=5)

    tk.Button(resultado_window, text="Guardar", command=lambda: guardar_decisiones(decisiones)).pack(pady=10)

def guardar_decisiones(decisiones):
    with open("registro_decisiones.json", "w") as archivo:
        json.dump(decisiones, archivo, indent=4)
