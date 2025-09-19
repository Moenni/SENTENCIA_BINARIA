
import json

def guardar_partida(decisiones, perfil, jugador_id="jugador1"):
    datos = {
        "decisiones": decisiones,
        "perfil": perfil
    }
    with open(f"partida_{jugador_id}.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_partida(jugador_id="jugador1"):
    try:
        with open(f"partida_{jugador_id}.json", "r") as archivo:
            datos = json.load(archivo)
        return datos["decisiones"], datos["perfil"]
    except FileNotFoundError:
        return [], {"confianza": 0, "anonimato": 0, "riesgo": 0}
