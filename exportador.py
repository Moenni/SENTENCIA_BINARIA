# exportador.py
import json
from perfil import generar_perfil
from decisiones import obtener_decisiones

perfil = generar_perfil()
decisiones = obtener_decisiones()

with open("datos_juego.json", "w", encoding="utf-8") as f:
    json.dump({"perfil": perfil, "decisiones": decisiones}, f, indent=4)
