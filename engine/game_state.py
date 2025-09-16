class GameState:
    def __init__(self):
        self.reputation = {"Nucleo": 0, "Fragmentos": 0}
        self.variables = {"autonomia": 0, "control": 0, "corrupcion": 0}
        self.scripts_unlocked = []
        self.decision_log = []  # ← Esto es clave para evitar el error

    def update(self, effects, context=None):
        # Aplicar efectos éticos y reputacionales
        for key, value in effects.items():
            if key in self.variables:
                self.variables[key] += value
            elif key in self.reputation:
                self.reputation[key] += value

        # Registrar decisión si hay contexto
        if context:
            self.decision_log.append(context)

    def summary(self):
        return {
            "Variables éticas": self.variables,
            "Reputación": self.reputation,
            "Scripts desbloqueados": self.scripts_unlocked,
            "Log de decisiones": self.decision_log
        }
