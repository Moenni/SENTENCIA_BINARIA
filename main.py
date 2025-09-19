from epilogo import mostrar_epilogo
from transiciones import animacion_carga
from engine.game_state import GameState
from engine.decision_tree import load_node, execute_decision
from perfil import mapear_valores, mostrar_perfil
from partida import guardar_partida, cargar_partida


def iniciar_juego():
    # Tu lógica original: inicializar estado, cargar nodo, pedir decisión, ejecutar y mostrar resumen
    
    print("🧠 Entrando a Sentencia Binaria...")  # Confirmación de inicio

    state = GameState()
    print("📦 Estado del juego inicializado")  # Confirmación de GameState
    # Al iniciar el juego (si se elige cargar):
    decisiones, perfil = cargar_partida()
    if decisiones:
        print("📂 Partida cargada con decisiones previas.")
        mostrar_perfil(perfil)
    else:
        print("🆕 Iniciando nueva partida.")


    current_node = load_node("eco_del_nucleo")
    if current_node:
        print("✅ Nodo cargado correctamente")  # Confirmación de carga
        current_node.present()

        decision = input("🧠 Elegí tu sentencia (A/B): ").strip().upper()
        print(f"📥 Decisión ingresada: {decision}")

        execute_decision(state, current_node, decision)
        decisiones = []
        decisiones.append({
            "momento": "eco_del_nucleo",
            "dilema": current_node.description,
            "elección": decision,
            "impacto": current_node.options[decision].get("effects", "Sin impacto definido")
        })
        print("📋 Decisiones registradas:", decisiones)

        print("\n📊 Estado actual:")
        print(state.summary())
          # ✅ Mostrar perfil y guardar partida
        impacto = current_node.options[decision].get("effects", {})
        perfil = mapear_valores(impacto)
        guardar_partida(decisiones, perfil)
        mostrar_perfil(perfil)



    else:
        print("⚠️ No se pudo cargar el nodo inicial.")
       

def main():
    mostrar_epilogo(lambda:animacion_carga(iniciar_juego))



if __name__ == "__main__":
    main()
