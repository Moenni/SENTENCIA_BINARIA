from engine.game_state import GameState
from engine.decision_tree import load_node, execute_decision

def main():
    print("🧠 Entrando a Sentencia Binaria...")  # Confirmación de inicio

    state = GameState()
    print("📦 Estado del juego inicializado")  # Confirmación de GameState

    current_node = load_node("eco_del_nucleo")
    if current_node:
        print("✅ Nodo cargado correctamente")  # Confirmación de carga
        current_node.present()

        decision = input("🧠 Elegí tu sentencia (A/B): ").strip().upper()
        print(f"📥 Decisión ingresada: {decision}")

        execute_decision(state, current_node, decision)

        print("\n📊 Estado actual:")
        print(state.summary())
    else:
        print("⚠️ No se pudo cargar el nodo inicial.")

if __name__ == "__main__":
    main()
