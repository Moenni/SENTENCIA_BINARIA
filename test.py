# test.py
from engine.decision_tree import load_node

node = load_node("eco_del_nucleo")
if node:
    node.present()
