import tkinter as tk
from estilo import aplicar_estilo, estilo_label

# 🧠 Traducción de valores narrativos a categorías éticas
def mapear_valores(impacto):
    traduccion = {
        "autonomia": "confianza",
        "control": "anonimato",
        "Fragmentos": "riesgo",
        "Nucleo": "riesgo"
    }

    perfil = {"confianza": 0, "anonimato": 0, "riesgo": 0}

    for clave, valor in impacto.items():
        categoria = traduccion.get(clave)
        if categoria:
            perfil[categoria] += valor

    return perfil

# 🧠 Interpretación filosófica del perfil
def interpretar_perfil(perfil):
    frases = []

    if perfil["confianza"] > perfil["anonimato"]:
        frases.append("Tu recorrido revela una inclinación hacia la transparencia y la autonomía.")
    elif perfil["anonimato"] > perfil["confianza"]:
        frases.append("Tu estilo privilegia la protección del sistema y el control sobre la exposición.")

    if perfil["riesgo"] > 0:
        frases.append("Has asumido riesgos éticos que podrían fragmentar el equilibrio del núcleo.")
    elif perfil["riesgo"] < 0:
        frases.append("Tu camino refleja una búsqueda de estabilidad y contención ética.")

    if not frases:
        frases.append("Tu perfil aún está en construcción. Cada decisión revelará más de tu esencia.")

    return "\n".join(frases)

# 🎨 Visualización gráfica y textual del perfil
def mostrar_perfil(perfil):
    ventana = tk.Tk()
    ventana.title("Tu Perfil Ético")
    aplicar_estilo(ventana)

    estilo_label("Tu Perfil Ético", ventana).pack(pady=10)

    interpretacion = interpretar_perfil(perfil)
    tk.Label(
        ventana,
        text=interpretacion,
        wraplength=400,
        fg="lightgray",
        bg="#1e1e1e",
        font=("Helvetica", 11),
        justify="left"
    ).pack(pady=20)

    tk.Label(
        ventana,
        text="Resumen de tus decisiones:",
        fg="white",
        bg="#1e1e1e",
        font=("Helvetica", 14)
    ).pack(pady=10)

    for clave, valor in perfil.items():
        tk.Label(
            ventana,
            text=f"{clave.capitalize()}: {valor} decisiones",
            fg="white",
            bg="#1e1e1e",
            font=("Helvetica", 12)
        ).pack(pady=5)

    # ✅ Visualización gráfica
    canvas = tk.Canvas(ventana, width=700, height=100, bg="#1e1e1e", highlightthickness=0)
    canvas.pack(pady=10)

    colores = {
        "confianza": "#4caf50",
        "anonimato": "#2196f3",
        "riesgo": "#f44336"
    }

    x = 20
    for clave, valor in perfil.items():
        largo = min(200, abs(valor) * 20)
        color = colores.get(clave, "gray")
        etiqueta = f"{clave.capitalize()} ({valor})"
        canvas.create_text(x + 100, 10, text=etiqueta, fill="white", font=("Helvetica", 10))
        canvas.create_rectangle(x, 30, x + largo, 50, fill=color)
        x += 220

    ventana.mainloop()