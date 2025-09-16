import json
from engine.modules import unlock_script

def load_node(node_id):
    print(f"📦 Intentando cargar nodo: {node_id}")

    try:
        with open("data/nodes.json", "r", encoding="utf-8") as f:
            nodes = json.load(f)
        return Node(nodes[node_id])
    except Exception as e:
        print(f"❌ Error al cargar el nodo: {e}")
        return None

class Node:
    def __init__(self,data):
        self.title= data["title"]
        self.description= data["description"]
        self.options= data["options"]
    def present(self):
        print(f"\n📍 {self.title}")
        print(f"{self.description}\n")
        for key in self.options:
            print(f"{key}: {self.options[key]['text']}")


def execute_decision(state,node,choice):
    if choice not in node.options:
        print("⚠️ Opción inválida.")
        return
    selected = node.options[choice]
    effects = selected.get("effects",{})
    context={
        "nodo":node.title,
        "decision":selected["text"],
        "efectos":effects
    }
    state.update(effects,context)
    
    script=selected.get("script")
    if script:
        unlock_script(state,script)
    print(f"\n✅ Decisión tomada: {selected['text']}")
    